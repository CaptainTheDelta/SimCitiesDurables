import random
import json

blocs = {}

with open("simcitydurable/data.json", 'r', encoding="utf-8") as file:
    blocs = json.load(file)

DATA_KEYS = [
    "production électricité",
    "production nourriture",
    "production eau",
    "production déchets industriels",
    "production déchets ménagers",
    "consommation énergie",
    "consommation nourriture",
    "consommation eau",
    "consommation déchets",
    "traitement eau",
    "traitement déchets industriels",
    "traitement déchets ménagers",
    "capacité hébergement",
    "capacité formation",
    "capacité emploi",
    "capacité transport",
    "santé hôpitaux",
    "santé EHPAD",
    "capacité commerces",
    "émissions CO2",
]

CATEGORIES = []

for b in blocs:
    c = blocs[b]["catégorie"]
    if c not in CATEGORIES:
        CATEGORIES.append(c)

class Board:
    def __init__(self, disp=[], rand=False):
        self.board = disp
        self.N = 10

        if disp == []:
            self.board = [["Vide" for i in range(self.N)] for j in range(self.N)]
            self.create_river(15)
            self.add_city_hall()
            self.add_parks(24)
        
        if rand:
            self.random_blocs()

    def __iter__(self):
        for x,row in enumerate(self.board):
            for y,cell in enumerate(row):
                yield (x,y),cell

    def create_river(self,n_blocks, max_around=1):        
        def cells_around(x, y, d=1):
            cells = []

            for i in range(-d, d):
                cells.extend([
                    (x-d, y+i),
                    (x+i, y+d),
                    (x+d, y-i),
                    (x-i, y-d)
                ])

            return cells

        def border_cells(N):
            cells = []

            for i in range(N-1):
                cells.extend([
                    (0, i),
                    (i, N-1),
                    (N-1, i+1),
                    (i+1, 0)
                ])

            return cells

        def in_board(cell): 
            return 0 <= cell[0] and cell[0] < self.N and 0 <= cell[1] and cell[1] < self.N

        def filter_in_board(cells):
            return list(filter(in_board, cells))

        def filter_candidates(cells):
            def around(cell):
                return river_counter[cell[0]][cell[1]] < max_around
            return list(filter(lambda cell: in_board(cell) and around(cell), cells))

        border = border_cells(self.N)
        river_counter = [[0 for i in range(self.N)] for j in range(self.N)]

        x,y = random.choice(border)
        river = [[(x,y), filter_candidates(cells_around(x,y))]]
        n = 1

        river_counter[x][y] = 9
        for rx,ry in river[0][1]:
            river_counter[rx][ry] = 1

        while n < n_blocks or not river[-1][0] in border:
            l = len(river[-1][1])

            if l == 0 or n == n_blocks:
                n -= 1
                x,y = river.pop(-1)[0]

                river_counter[x][y] -= 9
                for cx,cy in filter_in_board(cells_around(x,y)):
                    river_counter[cx][cy] -= 1

            else:
                n += 1
                x,y = river[-1][1].pop(random.randint(0, l-1))
                river.append([(x,y), filter_candidates(cells_around(x,y))])

                river_counter[x][y] += 9
                for cx,cy in filter_in_board(cells_around(x,y)):
                    river_counter[cx][cy] += 1

        for (x,y), cells in river:
            self.board[x][y] = "Riviere"

    def add_city_hall(self):
        liste = []
        for (x,y),bloc in self:
            if bloc == "Vide":
                liste.append((x,y))
        x,y = random.choice(liste)
        self.board[x][y] = "Mairie"

    def add_parks(self, n_parks):
        liste = []
        for (x,y),bloc in self:
            if bloc == "Vide":
                liste.append((x,y))
    
        for p in range(n_parks):
            x,y = random.choice(liste)
            i = liste.index((x,y))
            self.board[x][y] = "Parc"
            liste.pop(i)

    def random_blocs(self):
        blocs_names = list(blocs.keys())[4:]
        for (x,y),bloc in self:
            if bloc == "Vide":
                self.board[x][y] = random.choice(blocs_names)

