# SimCitiesDurables

## Pour l'exécution

1. changer le chemin vers l'excel aux endroits suivants :


*utils/sprite-generator.py* ligne 8
```python
from PIL import Image, ImageDraw, ImageFont
import os
import openpyxl as xl
import logging

logging.basicConfig(level=logging.DEBUG)

excel = r"/run/media/damien/SanDisk 32Go USB/PJT/2 - Jumeau Numérique/SimCities Numérique Excel-Python/plateau_excelV3.xlsx"
```

*simcitydurable/Bloc.y*, ligne 4
```python
import openpyxl as xl
from .Categorie import *

excel = r"/run/media/damien/SanDisk 32Go USB/PJT/2 - Jumeau Numérique/SimCities Numérique Excel-Python/plateau_excelV3.xlsx"
```

2. générer les images des cases avec `python utils/sprite-generator.py`

3. exécuter `python gui.py`

## Pour la regénération du fichier *simcitydurable/Bloc.py*

1. changer le chemin vers l'excel aux endroits suivants :


*utils/class-generator.py* ligne 8
```python
import openpyxl as xl
import logging

logging.basicConfig(level=logging.DEBUG)

output = r"/run/media/damien/SanDisk 32Go USB/PJT/tmp/simcitydurable/Bloc.py"

excel = r"/run/media/damien/SanDisk 32Go USB/PJT/2 - Jumeau Numérique/SimCities Numérique Excel-Python/plateau_excelV3.xlsx"
```

et ligne 78
```python
text = """import openpyxl as xl
from .Categorie import *

excel = r"/run/media/damien/SanDisk 32Go USB/PJT/2 - Jumeau Numérique/SimCities Numérique Excel-Python/plateau_excelV3.xlsx"
```