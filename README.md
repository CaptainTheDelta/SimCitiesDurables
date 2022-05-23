# SimCitiesDurables

## Fichier excel

Placez le fichier *plateau_excelV3.xlsx* dans `utils/res/`.


## Exécution des programmes

Il est nécessaire de se placer à la racine du projet pour une exécution correcte des programmes.

### Génération des images des cases
```
> python utils/sprite-generator.py
```

### Lancement du jeu
Il est nécessaire de générer les images avant de lancer le jeu.

```
> python gui.py
```


## Pour la regénération du fichier *simcitydurable/Bloc.py*

### Génération du fichier

```
> python utils/class-generator.py
```