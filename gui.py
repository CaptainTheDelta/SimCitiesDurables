from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from simcitydurable.Bloc import *
from simcitydurable.Game import *
import os


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
        root.attributes('-zoomed', True)
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
            bloc = cell.__class__.__name__
            drag = not isinstance(cell, Indispensable)
            drop = drag or isinstance(cell, Vide)
            c = Cell(bloc,self.board,drag, drop, self.app, self.board)
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
        for bloc in Bloc.__subclasses__()[4:]:
            bloc = bloc.__name__
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
        score = ttk.Label(self.app, text="Score")
        score.grid(column=1,row=1, sticky=(N, W, E, S))


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
    for bloc in Bloc.__subclasses__():
        bloc = bloc.__name__
        path = os.path.join(img_folder, bloc+".png")
        try:
            i = ImageTk.PhotoImage(Image.open(path))
        except:
            print(f"{path} non trouvé")
        else:
            img[bloc] = i

    app = SimCityDurableApp(root)
    root.mainloop()