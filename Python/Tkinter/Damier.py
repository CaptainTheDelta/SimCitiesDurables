##----- Importation des Modules -----##
from tkinter import *

#----- Creation de la fenetre d'aide -----#

def afficher_regle() :
    pass


def creation_fenetre_aide ():
   pass
    


##----- Variables globales -----##
c = 50                          # Longueur d'un côté d'une case
n = 10                          # Nombre de cases par ligne et par colonne
cases = []                      # Liste contenant les objets cases

##----- Création de la fenêtre -----##
fenetre_damier = Tk()
fenetre_damier.title('Damier')

##----- Création des canevas -----##
dessin = Canvas(fenetre_damier, width = n*c+2, height = n*c+2, bg = 'white')
dessin.pack()

##----- Création des figures -----##
for ligne in range(n):          # Les cases de chaque ligne seront stockées dans "transit"
    transit=[]
    for colonne in range(n):    # Conception des cases d'une ligne
        transit.append(dessin.create_rectangle(colonne*c+2, ligne*c+2, (colonne+1)*c+2, (ligne+1)*c+2))
    cases.append(transit)       # Ajout de la ligne à la liste principale


##----- Modification des cases  -----##
def clic (event):

    x=event.x
    y=event.y

    j= int(x/c)
    i= int(y/c)
    dessin.itemconfigure(cases[i][j], outline='green', fill='green')

def re_init():
    for i in range(n) :
        for j in range(n) :
            dessin.itemconfigure(cases[i][j], outline='black', fill='white')
    

    # un clic gauche sur la surface provoquera l'appel de la fonction clic()
dessin.bind('<Button-1>', clic)


#----- Création de barre de menu -----#

barre_fenetre_damier = Menu(fenetre_damier)
menu_fichier = Menu(barre_fenetre_damier, tearoff=0)
menu_fichier.add_command(label="réinitialiser", command=re_init)
menu_fichier.add_separator()
menu_fichier.add_command(label="fermer", command=fenetre_damier.destroy)
barre_fenetre_damier.add_cascade(label="Fichier", menu=menu_fichier)

menu_aide = Menu(barre_fenetre_damier, tearoff=0)
menu_aide.add_command(label="Aide", command=creation_fenetre_aide)
barre_fenetre_damier.add_cascade(label="Aide", menu=menu_aide)

fenetre_damier.config(menu=barre_fenetre_damier)


##----- Programme principal -----##
fenetre_damier.mainloop()                  # Boucle d'attente des événements  



    