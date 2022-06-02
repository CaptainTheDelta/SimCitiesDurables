##----- Importation des Modules -----##
from tkinter import *
from Consommation import *

#----- fonctions -----#

def afficher_regle () :
    detail = ''
    encart_droit = Canvas(fenetre_aide)
    encart_droit.grid(row = 0, column = 1, sticky = E)
    detail = ''
    detail += 'En début de partie un embryon de ville est créé,\n'
    detail += 'il comporte une rivière continue,des parcs et un hotel de ville.\n'
    detail += '\n Votre but est de placer vos blocs un à un pour batir votre ville.\n'
    detail += 'Le jeu fini lorsque toute les cases sont remplies.\n'
    detail += 'Votre but est de créer la ville la plus respectueuse de la nature \n'
    detail += 'Les points sont calculés à la fin\n'
    affichage_detail = Label(encart_droit, text = detail)
    affichage_detail.pack()

def afficher_notation () :
    detail = ''
    encart_droit = Canvas(fenetre_aide)
    encart_droit.grid(row = 0, column = 1, sticky = E)
    detail += 'la notation se fait sur 20 point est est découpée en 3 pans :\n'
    detail += '\n le Dimensionnement, la Pollution et la Disposition \n'
    detail += '\n le dimenssionnement le fait que la ville soit correctement équilibrée\n'
    detail += 'Les points sont calculés à la fin de la partie, en moyenne des 3 pans\n'
    affichage_detail = Label(encart_droit, text = detail)
    affichage_detail.pack()

def effacer () :
    detail = ''
    
    encart_droit = Canvas(fenetre_aide)
    encart_droit.grid(row = 0, column = 1, sticky = E)

def affiche_carc_batiment() :
    detail = 'ASAP'
    

#----- architecture fenetre aide -----#

fenetre_aide = Tk()
fenetre_aide.title('Aide')
    
encart = Frame(fenetre_aide)
encart.grid()

encart_gauche = Canvas(fenetre_aide)
encart_gauche.grid(row = 0, column = 0, sticky = W)

encart_droit = Canvas(fenetre_aide)
encart_droit.grid(row = 0, column = 1, sticky = E)
detail = ''
affichage_detail = Label(encart_droit, text = detail)
affichage_detail.grid()

bouton_regle = Button(encart_gauche, text='Règles', command=afficher_regle)
bouton_regle.grid(row = 1, column = 0)

bouton_notation = Button(encart_gauche, text='Notation', command=afficher_notation)
bouton_notation.grid(row = 2, column = 0)

bouton_effacer = Button(encart_gauche, text='Effacer', command=effacer)
bouton_effacer.grid(row = 3, column = 0)

#----- Création menu déroulant aide batiment -----#

liste_batiment = [
    "CentreCommercialUrbain",
    "CentreCommercialGrand",
    "CommerceProximitePetit",
    "CommerceProximiteGrand",
    ]

selection_bloc = StringVar(encart_gauche)
selection_bloc.set("details d'un bloc")

opt = OptionMenu(encart_gauche, selection_bloc, *liste_batiment)
opt.config(font=('Helvetica', 12))
opt.grid(column= 0)


titre_detail = Label(encart_droit, text="", font=('Helvetica', 12), fg='black')
titre_detail.grid(column = 1, row = 0)
caracteristique = Label(encart_droit, text=detail, font=('Helvetica', 12), fg='black')
caracteristique.grid(column = 1, row = 1)


def affiche_carc_batiment(*args) :
    caracteristique = "Le bloc détaillé {}".format(selection_bloc.get())
    caracteristique.join('\n {} = ASAP'.format(dir(selection_bloc.get())[i]) for i in range (26, 48)) # problème de join
    titre_detail.configure(text = caracteristique)

selection_bloc.trace("w", affiche_carc_batiment)

fenetre_aide.mainloop()

'''
dir(CentreCommercialUrbain)[26::]

donne

['capacite_commerce',
 'capacite_emploi',
 'capacite_formation',
 'capacite_hebergement',
 'capacite_soin_ehpad',
 'capacite_soin_hopital',
 'capacite_transport',
 'coefficient_co2',
 'consommation_dechet',
 'consommation_eau',
 'consommation_energie',
 'consommation_nourriture',
 'coordonnee',
 'emission_co2',
 'ordre',
 'production_dechet_industriel',
 'production_dechet_menager',
 'production_eau',
 'production_electricite',
 'production_nourriture',
 'traitement_dechet_industriel',
 'traitement_dechet_menager',
 'traitement_eau']