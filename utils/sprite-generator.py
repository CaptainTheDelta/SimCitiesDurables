from PIL import Image, ImageDraw, ImageFont
import os
import openpyxl as xl
import logging

logging.basicConfig(level=logging.DEBUG)
#============================ excel configuration =============================

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

name_exceptions = [
    ("groupes sc", "groupe scolaire"),
    ("station d'ép", "station épuration"),
    ("station de production d'e", "station eau potable"),
    ("groupement de ", "commerce de proximité"),
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

#============================ Image configuration =============================

n = 69
length = 500
output = "test.png"
draw_border = True

fonts_folder = "/usr/share/fonts/liberation-sans"
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


im = Image.new("RGB", (length*n,length*n), "white")
d = ImageDraw.Draw(im)

if draw_border:
    for i in range(1,n):
        d.line((0,i*length-1,n*length,i*length-1), fill="grey")
        d.line((i*length-1,0,i*length-1,n*length), fill="grey")


k = 0
for cat, (start, end) in xl_data.items():
    logging.info(f"Génération des blocs de catégorie {cat}.")
    for l in range(start, end+1):
        y,x = divmod(k, n)
        k += 1

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

        logging.debug(f"Bloc {name}")
        name = name[0].upper() + name[1:]

        regular_font = ImageFont.truetype(regular,s2)

        name,bold_font = wrap_text(name, bold, s)
        n_line = len(name.split('\n'))
        variant,regular_font = wrap_text(variant, regular, s2)

        d.text((px+x*length,py+y*length), name, font=bold_font, fill="black")
        height = bold_font.getsize_multiline(name)[1]
        
        d.text((px+x*length,py+height+y*length+delta), variant, font=regular_font, fill="grey")

im.save(output)

# https://stackoverflow.com/questions/16579674/using-spritesheets-in-tkinter