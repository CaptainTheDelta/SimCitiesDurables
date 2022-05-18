import openpyxl as xl
import logging

logging.basicConfig(level=logging.DEBUG)

output = r"/run/media/damien/SanDisk 32Go USB/PJT/tmp/simcitydurable/Bloc.py"

excel = r"/run/media/damien/SanDisk 32Go USB/PJT/2 - Jumeau Numérique/SimCities Numérique Excel-Python/plateau_excelV3.xlsx"
plateau_xl = xl.load_workbook(excel, read_only=True, data_only=True)
donnees = plateau_xl["Données"]

xl_data = {
    "Production d'énergie": [6, 15],
    "Habitation": [21, 30],
    "Santé": [36, 39],
    "Consommation": [45, 48],
    "Eau": [54, 59],
    "Education": [65, 66],
    "Transports": [72, 77],
    "Industrie": [83, 98],
    "Alimentation": [104, 110],
}

categories = {
    "Production d'énergie": "ProductionEnergie",
    "Habitation": "Habitation",
    "Santé": "Sante",
    "Consommation": "Consommation",
    "Eau": "Eau",
    "Education": "Education",
    "Transports": "Transport",
    "Industrie": "Industrie",
    "Alimentation": "Alimentation",
}

xl_coef_pollution = {
    "Production d'énergie": ['F', 8],
    "Habitation": ['H', 16],
    "Santé": ['J', 27],
    "Consommation": ['L', 32],
    "Eau": ['N', 37],
    "Education": ['O', 37],
    "Transports": ['P', 47],
    "Industrie": ['R', 54],
    "Alimentation": ['T', 71],
}


def replace_multiple(text, replacements):
    for f, r in replacements:
        text = text.replace(f, r)
    return text


name_exceptions = [
    ("groupes sc", "groupe scolaire"),
    ("station d'ép", "station épuration"),
    ("station de production d'e", "station eau potable"),
]

variant_methods = {
    "Production d'énergie": lambda v: v.split()[0],
    "Habitation": lambda v: v.split()[-1],
    "Santé": lambda v: v.split()[0],
    "Consommation": lambda v: v.split()[0],
    "Eau": lambda v: v.split()[0],
    "Education": lambda v: v,
    "Transports": lambda v: v,
    "Industrie": lambda v: v if v != "nouvelles technologies" else "nouvelle technologie",
    "Alimentation": lambda v: v.split()[0],
}



text = """import openpyxl as xl
from .Categorie import *

excel = r"/run/media/damien/SanDisk 32Go USB/PJT/2 - Jumeau Numérique/SimCities Numérique Excel-Python/plateau_excelV3.xlsx"
plateau_xl = xl.load_workbook(excel, read_only=True, data_only=True)
donnees = plateau_xl["Données"]
pollution = plateau_xl["Pollution"]

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
    "émissions CO2"
]

DATA_UNITES = [
    'MWh/an',
    'kg/an/bloc',
    'm3/an/bloc',
    't/an/bloc',
    't/an/bloc',
    'MWh/an',
    'kg/an/bloc',
    'm3/an/bloc',
    't/an/bloc',
    'm3/an/bloc',
    't/an/bloc',
    't/an/bloc',
    'personnes',
    'personnes',
    'personnes',
    'personnes',
    'personnes',
    'personnes',
    'personnes',
    'kgCO2'
]


class Bloc:
    def __init__(self, name, categorie, xl_data_line=0, xl_pollution_cell='A1'):
        self.name = name
        self.categorie = categorie
        if len(self.data) == 0:
            self.data["coefficient pollution"] = pollution[xl_pollution_cell].value if pollution[xl_pollution_cell].value != None else 0
            for k, cell in zip(DATA_KEYS, donnees[f"D{xl_data_line}:W{xl_data_line}"][0]):
                self.data[k] = cell.value if cell.value != None else 0

    def __repr__(self):
        return self.__class__.__name__

    def get(self, key):
        return self.data[key]


class Vide(Bloc, Indispensable):
    data = {}
    def __init__(self):
        super().__init__("Vide", "Indispensable")


class Riviere(Bloc, Indispensable):
    data = {}
    def __init__(self):
        super().__init__("Rivière", "Indispensable")


class Mairie(Bloc, Indispensable):
    data = {}
    def __init__(self):
        super().__init__("Mairie", "Indispensable")


class Parc(Bloc, Indispensable):
    data = {}
    def __init__(self):
        super().__init__("Parc", "Indispensable")

"""
for cat, (start, end) in xl_data.items():
    logging.info(f"Génération des blocs de catégorie {cat}.")
    text += "#" + f" {cat} ".center(78, '=') + "\n\n"
    for l in range(start, end+1):
        name = donnees[f"B{l}"].value
        variant = ""
        pollution_cell = xl_coef_pollution[cat][0] + str(xl_coef_pollution[cat][1]+l-start)

        if name == None or (l != end and donnees[f"B{l+1}"].value == None):
            variant = donnees[f"C{l}"].value

        lbis = l
        while name == None:
            lbis -= 1
            name = donnees[f"B{lbis}"].value

        for s, r in name_exceptions:
            if name.startswith(s):
                name = r

        if name.endswith('x') or name.endswith('s'):
            name = name[:-1]

        if variant != "":
            name += ' ' + variant_methods[cat](variant)
        name2 = name

        name = replace_multiple(
            name, [('é', 'e'), ('ô', 'o'), (" de ", " "), ("/", " "), ("d'", ' ')])
        name = name.title().replace(" ", "")

        logging.debug(f"Bloc {name}")
        text += f"""class {name}(Bloc, {categories[cat]}):
    data = {{}}
    def __init__(self):
        super().__init__("{name2}", "{cat}", {l}, "{pollution_cell}")


"""

with open(output, 'w', encoding='utf8') as file:
    file.write(text)