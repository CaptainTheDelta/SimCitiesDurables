import json
import openpyxl as xl
import logging

logging.basicConfig(level=logging.DEBUG)

output = r"simcitydurable/data.json"

excel = r"utils/res/plateau_excelV3.xlsx"
plateau_xl = xl.load_workbook(excel, read_only=True, data_only=True)
donnees = plateau_xl["Données"]
pollution = plateau_xl["Pollution"]

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


def simplified_name(name, variant):
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

    return name,name2


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

         
blocs = {}

for bloc in ["Vide", "Riviere", "Mairie", "Parc"]:
    blocs[bloc] = {
        "catégorie": "Indispensable",
        "nom": bloc,
        "nom simplifié": bloc,
        "coefficient pollution": 0,
    }
    
    for k in DATA_KEYS:
        blocs[bloc][k] = 0

blocs["Riviere"]["nom"] = "Rivière"
blocs["Riviere"]["nom simplifié"] = "Rivière"


for cat, (start, end) in xl_data.items():
    logging.info("")
    logging.info(f"Lecture des informations de la catégorie {cat}.")
    
    for l in range(start, end+1):
        name = donnees[f"B{l}"].value
        variant = ""
        
        data = {}

        # calcul de la position de la cellule contenant le coefficient pollution
        # dans l'onglet pollution de l'excel
        xl_pollution_cell = xl_coef_pollution[cat][0] + str(xl_coef_pollution[cat][1] + l - start)
        data["coefficient pollution"] = pollution[xl_pollution_cell].value if pollution[xl_pollution_cell].value != None else 0

        # lecture des différents coefficients dans l'onglet donnees (ligne l)
        for k, cell in zip(DATA_KEYS, donnees[f"D{l}:W{l}"][0]):
            data[k] = cell.value if cell.value != None else 0

        # détermination du nom du bloc
        if name == None or (l != end and donnees[f"B{l+1}"].value == None):
            variant = donnees[f"C{l}"].value

        lbis = l
        while name == None:
            lbis -= 1
            name = donnees[f"B{lbis}"].value

        name3 = name + " " + variant

        name, name2 = simplified_name(name, variant)
        logging.debug(f"Bloc {name}")

        data["catégorie"] = cat
        data["nom simplifié"] = name2
        data["nom"] = name3

        blocs[name] = data

with open(output, 'w', encoding='utf-8') as out:
    json.dump(blocs,out, indent=4, ensure_ascii=False)