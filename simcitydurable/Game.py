from .Bloc import *
from .Board import *

from pprint import pprint
from math import sqrt


DISTANCE_DE_REFERENCE = [
    0, 0, 5, 15, 31, 50, 65, 95, 135, 185, 250, 330, 420, 550, 680, 800, 1000
]

class Game:
    def __init__(self):
        self.board = Board(rand=True)
        self.note_dimmensionnement = self.calcul_note_dimensionnement()
        self.note_pollution = self.calcul_note_pollution()

    def calcul_ratios_note_dimensionnement(self, population):
        total = {}

        for k in DATA_KEYS:
            total[k] = 0
        
        for _, bloc in self.board:
            for k in DATA_KEYS:
                total[k] += bloc.get(k)
        return {
            "énergétique": total["production électricité"]/total["consommation énergie"],
            "nourriture": total["production nourriture"]/total["consommation nourriture"],
            "eau production": total["production eau"]/total["consommation eau"],
            "eau traitement": total["traitement eau"]/total["consommation eau"],
            "hébergement": total["capacité hébergement"]/population,
            "formation": total["capacité formation"]/(0.235*total["capacité hébergement"]),
            "santé EHPAD": total["santé EHPAD"]/(0.01*total["capacité hébergement"]),
            "santé hôpitaux": total["santé hôpitaux"]/(0.005*total["capacité hébergement"]),
            "déchets ménagers": total["traitement déchets ménagers"]/total["production déchets ménagers"],
            "déchets industriels": total["traitement déchets industriels"]/total["production déchets industriels"],
            "déchets réutilisés": total["consommation déchets"]/(0.2*(total["production déchets industriels"]+total["production déchets ménagers"])),
            "emploi": total["capacité emploi"]/(0.443*total["capacité hébergement"]),
            "transport": total["capacité transport"]/(0.5*total["capacité hébergement"]),
            "commerces": total["capacité hébergement"]/total["capacité commerces"]
        }

    points = {
        0.5: ("commerces",),
        1.0: ("eau traitement", "transport", "déchets réutilisés"),
        1.5: ("emploi", "formation", "déchets ménagers", "déchets industriels"),
        1.75: ("nourriture", "eau production", "hébergement", "énergétique", "santé hôpitaux", "santé EHPAD")
    }

    def calcul_note_dimensionnement(self, population=100000):
        note = 0
        ratios = self.calcul_ratios_note_dimensionnement(population)
        pprint(ratios)

        for p in self.points:
            print(self.points[p])
            for r in self.points[p]:
                if abs(ratios[r]-1) <= 0.1:
                    note += p

        return note

    def calcul_note_pollution_categories(self):
        notes = {}
        for c in CATEGORIES:
            notes[c] = [0, 0]
        for _, bloc in self.board:
            c = bloc.categorie
            notes[c][0] += bloc.get("émissions CO2") * \
                bloc.get("coefficient pollution")
            notes[c][1] += bloc.get("émissions CO2")
        for c in CATEGORIES:
            if notes[c][1] == 0:
                notes[c] = 0
            else:
                notes[c] = notes[c][0] / notes[c][1]
        return notes

    def calcul_note_pollution(self):
        return sum(self.calcul_note_pollution_categories().values())

    def note_disposition(self):
        buildings = {}
        ratios = {}
        points = {}
        categories_eclatement = [
            "Habitation", "Industrie", "Transport", 
            "Education", "Production d'énergie", "Consommation"
        ]

        for c in categories_eclatement:
            buildings[c] = []
            points["Eclatement "+c] = 0
        
        for coords,_ in self.board:
            buildings[c].append(coords)
        
        for c in categories_eclatement:
            l = len(buildings[c])
            distance = 0
            while len(buildings[c]) > 0:
                bloc1 = buildings[c].pop()
                for bloc2 in buildings[c]:
                    distance += sqrt( (bloc2[0]-bloc1[0])**2 + (bloc2[1]-bloc1[1])**2)
            ratios[c] = distance / DISTANCE_DE_REFERENCE[l]

            if ratios[c] > 1:
                points["Eclatement "+c] = 1 # TODO ou /!\ 0.5 /!\
                
        return sum(ratios.values())

        