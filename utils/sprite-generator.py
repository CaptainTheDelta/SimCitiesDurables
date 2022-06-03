from PIL import Image, ImageDraw, ImageFont
import os
import openpyxl as xl
import logging

logging.basicConfig(level=logging.DEBUG)

excel = r"utils/res/plateau_excelV3.xlsx"
plateau_xl = xl.load_workbook(excel, read_only=True, data_only=True)
donnees = plateau_xl["Données"]

#============================ Image configuration =============================

n = 69
length = 100
draw_border = True
fonts_folder = "utils/fonts"
regular = os.path.join(fonts_folder, "LiberationSans-Italic.ttf")
bold = os.path.join(fonts_folder, "LiberationSans-Bold.ttf")

#==================================== main ====================================

n = int((n**0.5)//1 + 1)
s = length // 5
s2 = length // 6
px = length // 40
py = 0
delta = 10

def wrap_text(text, font_path, size):
    lines = ['']
    font = ImageFont.truetype(font_path,size)

    for word in text.split():
        if font.getlength(lines[-1] + ' ' + word) < (length - 2*px):
            lines[-1] += ' ' + word
        else:
            while font.getlength(lines[-1]) > (length - 2*px):
                size -= 1
                font = ImageFont.truetype(font_path, size)

            lines.append(word)
        while font.getlength(lines[-1]) > (length - 2*px):
            size -= 1
            font = ImageFont.truetype(font_path, size)

    return '\n'.join(lines).strip(),font


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

colors = {
    "Production d'énergie": "LightGoldenRodYellow",
    "Habitation": "LightGreen",
    "Santé": "LightPink",
    "Consommation": "LightSalmon",
    "Eau": "LightBlue",
    "Education": "LightCyan",
    "Transports": "LightGrey",
    "Industrie": "LightSteelBlue",
    "Alimentation": "gold",
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

# rivière :
Image.new("RGB", (length,length), "blue").save("utils/img/Riviere.png")
# mairie :
Image.new("RGB", (length,length), "red").save("utils/img/Mairie.png")
# parc :
Image.new("RGB", (length,length), "green").save("utils/img/Parc.png")
# parc :
Image.new("RGB", (length,length), "white").save("utils/img/Vide.png")



for cat, (start, end) in xl_data.items():
    logging.info(f"Génération des images de catégorie {cat}.")
    for l in range(start, end+1):
        im = Image.new("RGB", (length,length), colors[cat])
        d = ImageDraw.Draw(im)
        name = donnees[f"B{l}"].value
        variant = ""

        if name == None or (l != end and donnees[f"B{l+1}"].value == None):
            variant = donnees[f"C{l}"].value

        lbis = l
        while name == None:
            lbis -= 1
            name = donnees[f"B{lbis}"].value

        for e, r in name_exceptions:
            if name.startswith(e):
                name = r

        if name.endswith('x') or name.endswith('s'):
            name = name[:-1]
        
        n2 = name

        if variant != "":
            n2 += ' ' + variant_methods[cat](variant)

        n2 = replace_multiple(
            n2, [('é', 'e'), ('ô', 'o'), (" de ", " "), ("/", " "), ("d'", ' ')])
        n2 = n2.title().replace(" ", "")

        logging.debug(f"Bloc {name}")
        name = name[0].upper() + name[1:]

        regular_font = ImageFont.truetype(regular,s2)

        name,bold_font = wrap_text(name, bold, s)
        n_line = len(name.split('\n'))
        variant,regular_font = wrap_text(variant, regular, s2)

        d.text((px,py), name, font=bold_font, fill="black")
        height = bold_font.getsize_multiline(name)[1]
        
        d.text((px,py+height+delta), variant, font=regular_font, fill="grey")

        im.save("utils/img/"+n2+".png")