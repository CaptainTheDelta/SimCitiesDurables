from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from simcitydurable.Bloc import *
from simcitydurable.Game import *


img_folder = "./utils/img/"

size = 100 #px

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

        app = ttk.Frame(root, style='app.TFrame')
        app.grid(column=0,row=0, sticky=(N, W, E, S))
        app.rowconfigure(0, weight=1)
        app.columnconfigure(1, weight=1)

        # chargement des images des blocs
        self.img = {}
        for bloc in Bloc.__subclasses__():
            bloc = bloc.__name__
            try:
                i = ImageTk.PhotoImage(Image.open(img_folder+bloc+".png"))
            except:
                print(f"{img_folder+bloc}.png non trouvé")
            else:
                self.img[bloc] = i

        # création d'un jeu
        self.g = Game()

        # plateau
        self.board = ttk.Frame(app, width=10*size, height=10*size)
        self.board.grid(column=1,row=0)

        for (x,y),cell in self.g.board:
            c = Canvas(self.board,height=size,width=size)
            c.create_image(0,0,anchor=NW,image=self.img[cell.__class__.__name__])
            c.grid(row=x,column=y)



        # Bibliothèque de blocs
        self.lib_frame = ttk.Frame(app)
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
            if bloc in self.img:
                c = Canvas(self.lib,height=size,width=size)
                c.create_image(0,0,anchor=NW,image=self.img[bloc])
                row,column = divmod(k, 3)
                c.grid(row=row,column=column)
                k += 1

        self.lib_canvas.grid(column=0, row=0, sticky=(N, W, S))
        scrollbar.grid(column=1, row=0, sticky=(N, E, S))

        self.lib_frame.bind('<Enter>', self._bound_to_mousewheel)
        self.lib_frame.bind('<Leave>', self._unbound_to_mousewheel)

        # Zone d'affichage des scores
        score = ttk.Label(app, text="Score")
        score.grid(column=1,row=1, sticky=(N, W, E, S))

        self.app = app


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
    app = SimCityDurableApp(root)
    root.mainloop()