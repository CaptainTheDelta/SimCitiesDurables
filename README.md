# SimCitiesDurables

## Pour l'exécution

### Emplacement du fichier excel

Commencez par changer le chemin vers l'excel aux endroits suivants :


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

### Génération des images des cases

```
> python utils/sprite-generator.py
```

### Lancement du jeu

```
> python gui.pyy
```


## Pour la regénération du fichier *simcitydurable/Bloc.py*

### Emplacement du fichier excel

Changez le chemin vers l'excel aux endroits suivants :


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

### Génération du fichier

```
> python utils/class-generator.py
```