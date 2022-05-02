from tkinter import *
from tkinter import ttk


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



# plateau

board = ttk.Frame(app, width=1000, height=1000)
board['borderwidth'] = 4
board['relief'] = 'sunken'
board.grid(column=1,row=0)



# Bibliothèque de blocs

lib = ttk.Frame(app,width=200)
lib['borderwidth'] = 4
lib['relief'] = 'sunken'
lib.grid(column=0, row=0, sticky=(N, W, S), rowspan=2)



# Zone d'affichage des scores

score = ttk.Label(app, text="Score")
score.grid(column=1,row=1, sticky=(N, W, E, S))

root.mainloop()