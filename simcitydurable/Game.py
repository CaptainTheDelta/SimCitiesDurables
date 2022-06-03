from .Board import *

from pprint import pprint
from math import sqrt


DISTANCE_DE_REFERENCE = [
    0, 0, 5, 15, 31, 50, 65, 95, 135, 185, 250, 330, 420, 550, 680, 800, 1000
]

def calc_ratio(v1,v2):
    """Calcule le ratio de v1 par v2 en renvoyant 0 si v2 est nul."""
    if v2 == 0:
        return 0
    return v1/v2 

class Game:
    def __init__(self):
        self.board = Board()
        self.note_dimmensionnement = self.calcul_note_dimensionnement()
        self.note_pollution = self.calcul_note_pollution()

    def calcul_ratios_note_dimensionnement(self, population):
        total = {}

        for k in DATA_KEYS:
            total[k] = 0
        
        for _, bloc in self.board:
            for k in DATA_KEYS:
                total[k] += blocs[bloc][k]
        return {
            "énergétique": calc_ratio(total["production électricité"], total["consommation énergie"]),
            "nourriture": calc_ratio(total["production nourriture"], total["consommation nourriture"]),
            "eau production": calc_ratio(total["production eau"], total["consommation eau"]),
            "eau traitement": calc_ratio(total["traitement eau"], total["consommation eau"]),
            "hébergement": calc_ratio(total["capacité hébergement"], population),
            "formation": calc_ratio(total["capacité formation"], (0.235*total["capacité hébergement"])),
            "santé EHPAD": calc_ratio(total["santé EHPAD"], (0.01*total["capacité hébergement"])),
            "santé hôpitaux": calc_ratio(total["santé hôpitaux"], (0.005*total["capacité hébergement"])),
            "déchets ménagers": calc_ratio(total["traitement déchets ménagers"], total["production déchets ménagers"]),
            "déchets industriels": calc_ratio(total["traitement déchets industriels"], total["production déchets industriels"]),
            "déchets réutilisés": calc_ratio(total["consommation déchets"], (0.2*(total["production déchets industriels"]+total["production déchets ménagers"]))),
            "emploi": calc_ratio(total["capacité emploi"], (0.443*total["capacité hébergement"])),
            "transport": calc_ratio(total["capacité transport"], (0.5*total["capacité hébergement"])),
            "commerces": calc_ratio(total["capacité hébergement"], total["capacité commerces"])
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

        for p in self.points:
            for r in self.points[p]:
                if abs(ratios[r]-1) <= 0.1:
                    note += p

        return note

    def calcul_note_pollution_categories(self):
        notes = {}
        for c in CATEGORIES:
            # [numérateur, dénominateur]
            notes[c] = [0, 0]
        for _, bloc in self.board:
            c = blocs[bloc]["catégorie"]
            notes[c][0] += blocs[bloc]["émissions CO2"] * blocs[bloc]["coefficient pollution"]
            notes[c][1] += blocs[bloc]["émissions CO2"]
        for c in CATEGORIES:
            notes[c] = calc_ratio(*notes[c])
        return notes

    def calcul_note_pollution(self):
        return sum(self.calcul_note_pollution_categories().values())

    def calcul_note_disposition(self):
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
        
        for coords,b in self.board:
            c = blocs[b]["catégorie"]
            if c in categories_eclatement:
                buildings[c].append(coords)
        
        for c in categories_eclatement:
            l = len(buildings[c])
            distance = 0
            print(buildings[c])
            while len(buildings[c]) > 0:
                bloc1 = buildings[c].pop()
                for bloc2 in buildings[c]:
                    distance += sqrt( (bloc2[0]-bloc1[0])**2 + (bloc2[1]-bloc1[1])**2)
            print(l,DISTANCE_DE_REFERENCE)

            ratios[c] = calc_ratio(distance, DISTANCE_DE_REFERENCE[l])

            if ratios[c] > 1:
                points["Eclatement "+c] = 1 # TODO ou /!\ 0.5 /!\
                
        return sum(ratios.values())

    def update_notes(self):
        self.note_dimmensionnement = self.calcul_note_dimensionnement()
        self.note_pollution = self.calcul_note_pollution()

    def get_notes(self):
        self.update_notes()
        return (self.note_dimmensionnement, self.note_pollution, 0)