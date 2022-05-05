from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from simcitydurable.Bloc import *
from simcitydurable.Game import *

# Partie principale

root = Tk()
root.title("SimCityDurable")
root.attributes('-zoomed', True)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


menu_bar = Menu(root)

menu_file = Menu(menu_bar, tearoff=0)
menu_file.add_command(label="Quitter")

menu_tools = Menu(menu_bar, tearoff=0)
menu_tools.add_command(label="JSP frero")

menu_about = Menu(menu_bar, tearoff=0)
menu_about.add_command(label="Aide")

menu_bar.add_cascade(menu=menu_file, label="Fichier")
menu_bar.add_cascade(menu=menu_tools, label="Outils")
menu_bar.add_cascade(menu=menu_about, label="A propos")

root.config(menu=menu_bar)


s = ttk.Style()
# Create style used by default for all Frames
s.configure('app.TFrame', background='white')

app = ttk.Frame(root, style='app.TFrame')
app.grid(column=0,row=0, sticky=(N, W, E, S))
app.rowconfigure(0, weight=1)
app.columnconfigure(1, weight=1)

# chargement des images des blocs

img_folder = "utils/img/"
img = {}

for bloc in Bloc.__subclasses__():
    bloc = bloc.__name__
    try:
        i = ImageTk.PhotoImage(Image.open(img_folder+bloc+".png"))
    except:
        print(f"{img_folder+bloc}.png non trouvé")
    else:
        img[bloc] = i
        

# plateau

board = ttk.Frame(app, width=1000, height=1000)
board['borderwidth'] = 4
board['relief'] = 'sunken'
board.grid(column=1,row=0)



size = 100 #px

im = Image.new("RGB", (size,size), "white")
im.save('white.jpg')

vide = ImageTk.PhotoImage(Image.open("white.jpg"))

g = Game()

for (x,y),cell in g.board:
    c = Canvas(board,height=size,width=size)
    c.create_image(0,0,anchor=NW,image=img[cell.__class__.__name__])
    c.grid(row=x,column=y)



# Bibliothèque de blocs

lib_frame = ttk.Frame(app)
lib_frame.grid(column=0, row=0, sticky=(N, W, S),rowspan=2)
lib_frame.rowconfigure(index=0, weight=1)

lib_canvas = Canvas(lib_frame, background="yellow")
scrollbar = ttk.Scrollbar(lib_frame, orient="vertical", command=lib_canvas.yview)

lib = ttk.Frame(lib_canvas)
lib['borderwidth'] = 4
lib['relief'] = 'sunken'
lib.grid(column=0, row=0)

lib.bind(
    "<Configure>",
    lambda e: lib_canvas.configure(
        scrollregion=lib_canvas.bbox("all"),
        width=e.width
    )
)

lib_canvas.create_window((0, 0), window=lib, anchor="nw")
lib_canvas.configure(yscrollcommand=scrollbar.set)

k = 0
for bloc in Bloc.__subclasses__():
    bloc = bloc.__name__
    if bloc in img:
        c = Canvas(lib,height=size,width=size)
        c.create_image(0,0,anchor=NW,image=img[bloc])
        row,column = divmod(k, 3)
        c.grid(row=row,column=column)
        k += 1

lib_canvas.grid(column=0, row=0, sticky=(N, W, S))
scrollbar.grid(column=1, row=0, sticky=(N, E, S))


# Zone d'affichage des scores

score = ttk.Label(app, text="Score")
score.grid(column=1,row=1, sticky=(N, W, E, S))

root.mainloop()