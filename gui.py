from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from simcitydurable.Game import *
import os
()

img_folder = os.path.join(os.getcwd(),"utils/img")

size = 100 #px


class Cell(Canvas):
    def __init__(self,bloc,parent, drag, drop, app, board, *args, **kwargs):
        super().__init__(parent, width=size,height=size, *args, **kwargs)
        self.create_image(0,0,anchor=NW,image=img[bloc])
        self.bloc = bloc
        self.x = 0
        self.y = 0
        self.app = app
        self.board = board
        
        self.drag = drag
        self.drop = drop

        if self.drag:
            self.bind("<ButtonPress-1>", self.on_start)
            self.bind("<B1-Motion>", self.on_drag)
            self.bind("<ButtonRelease-1>", self.on_drop)
            self["cursor"] = "hand1"

    def on_start(self, event):
        self.icone = Canvas(self.app, width=size, height=size)
        self.icone.create_image(0,0,anchor=NW,image=img[self.bloc])
        self.x = self.app.winfo_rootx() + event.x
        self.y = self.app.winfo_rooty() + event.y
        self.on_drag(event)
        
        self.row = self.grid_info()['row'] 
        self.column = self.grid_info()['column']

        if self.drop:
            vide = Cell("Vide", self.board, False, True, self.app, self.board)
            vide.grid(row=self.row, column=self.column)


    def on_drag(self, event):
        xd = self.app.winfo_pointerx() - self.x
        yd = self.app.winfo_pointery() - self.y
        self.icone.place(x=xd,y=yd)

    def on_drop(self, event):
        self.icone.destroy()
        x,y = event.widget.winfo_pointerxy()
        target = event.widget.winfo_containing(x,y)
        
        if isinstance(target,Cell) and target.drop:
            row_target = target.grid_info()['row'] 
            column_target = target.grid_info()['column']

            c = Cell(self.bloc, self.board, True, True, self.app, self.board)
            c.grid(row=row_target, column=column_target)
        else:
            self.grid(row=self.row, column=self.column)


# Application
class SimCityDurableApp:
    def __init__(self, root):
        # configuration de la fenêtre
        root.title("SimCityDurable")
        #root.attributes('-zoomed', True)
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        # menus déroulants
        menu_bar = Menu(root)

        menu_file = Menu(menu_bar, tearoff=0)
        menu_file.add_command(label="Quitter")

        menu_tools = Menu(menu_bar, tearoff=0)
        menu_tools.add_command(label="Regénérer")

        menu_about = Menu(menu_bar, tearoff=0)
        menu_about.add_command(label="Aide")

        menu_bar.add_cascade(menu=menu_file, label="Fichier")
        menu_bar.add_cascade(menu=menu_tools, label="Outils")
        menu_bar.add_cascade(menu=menu_about, label="A propos")

        root.config(menu=menu_bar)

        # fenêtre sous le menu
        s = ttk.Style()
        s.configure('app.TFrame', background='white')

        self.app = ttk.Frame(root, style='app.TFrame')
        self.app.grid(column=0,row=0, sticky=(N, W, E, S))
        self.app.rowconfigure(0, weight=1)
        self.app.columnconfigure(1, weight=1)


        # création d'un jeu
        self.g = Game()

        # plateau
        self.board = ttk.Frame(self.app, width=10*size, height=10*size)
        self.board.grid(column=1,row=0)

        for (x,y),cell in self.g.board:
            drag = blocs[cell]["catégorie"] != "Indispensable"
            drop = drag or cell == "Vide"
            c = Cell(cell,self.board,drag, drop, self.app, self.board)
            c.grid(row=x,column=y)



        # Bibliothèque de blocs
        self.lib_frame = ttk.Frame(self.app)
        self.lib_frame.grid(column=0, row=0, sticky=(N, W, S),rowspan=2)
        self.lib_frame.rowconfigure(index=0, weight=1)

        self.lib_canvas = Canvas(self.lib_frame)
        scrollbar = ttk.Scrollbar(self.lib_frame, orient="vertical", command=self.lib_canvas.yview)

        self.lib = ttk.Frame(self.lib_canvas)
        self.lib.grid(column=0, row=0)

        self.lib.bind(
            "<Configure>",
            lambda e: self.lib_canvas.configure(
                scrollregion=self.lib_canvas.bbox("all"),
                width=e.width
            )
        )

        self.lib_canvas.create_window((0, 0), window=self.lib, anchor="nw")
        self.lib_canvas.configure(yscrollcommand=scrollbar.set)

        k = 0
        blocs_list = list(blocs.keys())

        for bloc in blocs_list[4:]:
            if bloc in img:
                c = Cell(bloc,self.lib,True, False, self.app, self.board)
                row,column = divmod(k, 3)
                c.grid(row=row,column=column)
                k += 1

        self.lib_canvas.grid(column=0, row=0, sticky=(N, W, S))
        scrollbar.grid(column=1, row=0, sticky=(N, E, S))

        self.lib_frame.bind('<Enter>', self._bound_to_mousewheel)
        self.lib_frame.bind('<Leave>', self._unbound_to_mousewheel)

        # Zone d'affichage des scores
        self.scores_frame = ttk.Frame(self.app)
        self.scores_title = ttk.Label(self.scores_frame, text="Scores")
        self.scores_title.grid(column=0, row=0, sticky=(N, W, E), columnspan=2)
        
        self.score_dimensionnement_label = ttk.Label(self.scores_frame, text="Score dimensionnement")
        self.score_pollution_label = ttk.Label(self.scores_frame, text="Score pollution")
        self.score_disposition_label = ttk.Label(self.scores_frame, text="Score disposition")
        self.score_final_label = ttk.Label(self.scores_frame, text="Score final")
        self.score_dimensionnement_label.grid(row=1, column=0, sticky=E)
        self.score_pollution_label.grid(row=2, column=0, sticky=E)
        self.score_disposition_label.grid(row=3, column=0, sticky=E)
        self.score_final_label.grid(row=2, column=3, sticky=E)

        self.score_dimensionnement = StringVar(value='0')
        self.score_pollution = StringVar(value='0')
        self.score_disposition = StringVar(value='0')
        self.score_final = StringVar(value='0')

        self.score_dimensionnement_display = ttk.Label(self.scores_frame, textvariable=self.score_dimensionnement, width=4)
        self.score_pollution_display = ttk.Label(self.scores_frame, textvariable=self.score_pollution, width=4)
        self.score_disposition_display = ttk.Label(self.scores_frame, textvariable=self.score_disposition, width=4)
        self.score_final_display = ttk.Label(self.scores_frame, textvariable=self.score_final, width=4)
        self.score_dimensionnement_display.grid(row=1, column=1, sticky=E)
        self.score_pollution_display.grid(row=2, column=1, sticky=E)
        self.score_disposition_display.grid(row=3, column=1, sticky=E)
        self.score_final_display.grid(row=2, column=4, sticky=E)

        self.score_sur_20_1 = ttk.Label(self.scores_frame, text="/20")
        self.score_sur_20_2 = ttk.Label(self.scores_frame, text="/20")
        self.score_sur_20_3 = ttk.Label(self.scores_frame, text="/20")
        self.score_sur_20_4 = ttk.Label(self.scores_frame, text="/20")
        self.score_sur_20_1.grid(row=1, column=2, sticky=W)
        self.score_sur_20_2.grid(row=2, column=2, sticky=W)
        self.score_sur_20_3.grid(row=3, column=2, sticky=W)
        self.score_sur_20_4.grid(row=2, column=5, sticky=W)


        self.scores_frame.grid(row=1, column=1, sticky=(E,S,W))


    def _bound_to_mousewheel(self, event):
        self.lib_frame.bind_all("<Button-4>", self._on_mousewheel)
        self.lib_frame.bind_all("<Button-5>", self._on_mousewheel)
        self.lib_frame.bind_all("<Motion>", self._on_motion)


    def _unbound_to_mousewheel(self, event):
        self.lib_frame.unbind_all("<Button-4>")
        self.lib_frame.unbind_all("<Button-5>")
        self.lib_frame.unbind_all("<Motion>")


    def _on_motion(self, event):
        pass


    def _on_mousewheel(self, event):
        i = (event.num-4)*2-1
        self.lib_canvas.yview_scroll(i, "units")



if __name__ == "__main__":
    root = Tk()

# chargement des images des blocs
    img = {}
    for bloc in blocs.keys():
        path = os.path.join(img_folder, bloc+".png")
        try:
            i = ImageTk.PhotoImage(Image.open(path))
        except:
            print(f"{path} non trouvé")
        else:
            img[bloc] = i

    app = SimCityDurableApp(root)
    root.mainloop()