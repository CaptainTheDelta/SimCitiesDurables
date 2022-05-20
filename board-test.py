from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from random import choice


class Cell(Canvas):
    def __init__(self,color,parent, drag, drop,*args, **kwargs):
        super().__init__(parent, *args, background=color, **kwargs)
        self.color = color
        self.parent = parent
        self.x = 0
        self.y = 0
        
        self.drag = drag
        self.drop = drop
        print(parent,color,drop)

        if self.drag:
            self.bind("<ButtonPress-1>", self.on_start)
            self.bind("<B1-Motion>", self.on_drag)
            self.bind("<ButtonRelease-1>", self.on_drop)
            self["cursor"] = "hand1"

    def on_start(self, event):
        self.icone = Canvas(app, width=size, height=size, background=self.color)
        self.x = root.winfo_rootx() + event.x
        self.y = root.winfo_rooty() + event.y
        self.on_drag(event)
        
        self.row = self.grid_info()['row'] 
        self.column = self.grid_info()['column']

        if self.drop:
            print("drop!", self.parent)
            vide = Cell("white", board, False, True, width=size,height=size)
            vide.grid(row=self.row, column=self.column)



    def on_drag(self, event):
        xd = root.winfo_pointerx() - self.x
        yd = root.winfo_pointery() - self.y
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


colors = ["white","blue","yellow","orange","purple","cyan","green", "red", "pink", "magenta"]

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


# Bibliothèque de blocs
lib_frame = ttk.Frame(app)
lib_frame.grid(column=0, row=0, sticky=(N, W, S))
lib_frame.rowconfigure(index=0, weight=1)

lib_canvas = Canvas(lib_frame)
scrollbar = ttk.Scrollbar(lib_frame, orient="vertical", command=lib_canvas.yview)

lib = ttk.Frame(lib_canvas)
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



for x,color in enumerate(colors[2:]):
    c = Cell(color, lib, drag=True, drop=False, width=size,height=size)
    c.grid(row=x)



lib_canvas.grid(column=0, row=0, sticky=(N, W, S))
scrollbar.grid(column=1, row=0, sticky=(N, E, S))

def _bound_to_mousewheel(event):
    lib_frame.bind_all("<Button-4>", _on_mousewheel)
    lib_frame.bind_all("<Button-5>", _on_mousewheel)
    lib_frame.bind_all("<Motion>", _on_motion)


def _unbound_to_mousewheel(event):
    lib_frame.unbind_all("<Button-4>")
    lib_frame.unbind_all("<Button-5>")
    lib_frame.unbind_all("<Motion>")


def _on_motion(event):
    pass


def _on_mousewheel(event):
    i = (event.num-4)*2-1
    lib_canvas.yview_scroll(i, "units")


lib_frame.bind('<Enter>', _bound_to_mousewheel)
lib_frame.bind('<Leave>', _unbound_to_mousewheel)





root.mainloop()