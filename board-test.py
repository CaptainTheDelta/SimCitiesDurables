from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from random import choice


class Cell(Canvas):
    def __init__(self,color,parent, drag, drop, *args, **kwargs):
        super().__init__(parent, *args, background=color, **kwargs)
        self.color = color
        self.parent = parent
        self.x = 0
        self.y = 0
        
        self.drag = drag
        self.drop = drop

        if self.drag:
            self.bind("<ButtonPress-1>", self.on_start)
            self.bind("<B1-Motion>", self.on_drag)
            self.bind("<ButtonRelease-1>", self.on_drop)
            self["cursor"] = "hand1"

    def on_start(self, event):
        self.icone = Canvas(app, width=size, height=size, background=self.color)
        self.x = self.winfo_x() - event.x
        self.y = self.winfo_y() - event.y
        self.on_drag(event)
        
        self.row = self.grid_info()['row'] 
        self.column = self.grid_info()['column']

        vide = Cell("white", board, False, True, width=size,height=size)
        vide.grid(row=self.row, column=self.column)
        self.on_drag(event)


    def on_drag(self, event):
        xd = self.x + event.x
        yd = self.y + event.y
        self.icone.place(x=xd,y=yd)

    def on_drop(self, event):
        self.icone.destroy()
        x,y = event.widget.winfo_pointerxy()
        target = event.widget.winfo_containing(x,y)
        
        if isinstance(target,Cell) and target.drop:
            row_target = target.grid_info()['row'] 
            column_target = target.grid_info()['column']

            c = Cell(self.color, board, self.drag, self.drop, width=size,height=size)
            c.grid(row=row_target, column=column_target)
        else:
            self.grid(row=self.row, column=self.column)

# Partie principale

root = Tk()
root.title("test plateau")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

app = ttk.Frame(root)
app.grid(column=0,row=0)
app.rowconfigure(0, weight=1)
app.columnconfigure(1, weight=1)


colors = ["white","blue","yellow","orange","purple","cyan","green", "red"]

# plateau
size = 100 #px
n_cells = 4

board = ttk.Frame(app, width=n_cells*size, height=n_cells*size)
board.grid(row=0, column=1)

for x in range(n_cells):
    for y in range(n_cells):
        color = choice(colors)
        drag = not color in ["white", "blue"]
        drop=not color in ["blue"]
        c = Cell(color, board, drag, drop, width=size,height=size)
        c.grid(row=x,column=y)

# lib

# lib = ttk.Frame(app)
# lib.grid(row=0, column=0)


# for x,color in enumerate(colors[2:]):
#     c = Cell(color, lib, drag=True, drop=False, width=size,height=size)
#     c.grid(row=x)


root.mainloop()