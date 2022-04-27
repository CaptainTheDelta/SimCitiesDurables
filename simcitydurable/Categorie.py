class Categorie:
    pass

class Indispensable(Categorie):
    categorie_name = "Indispensable"

class ProductionEnergie(Categorie):
    categorie_name = "Production d'énergie"

class Habitation(Categorie):
    categorie_name = "Habitation"
    
class Sante(Categorie):
    categorie_name = "Santé"
    
class Consommation(Categorie):
    categorie_name = "Consommation"

class Eau(Categorie):
    categorie_name = "Eau"

class Education(Categorie):
    categorie_name = "Education"

class Transport(Categorie):
    categorie_name = "Transports"
    
class Industrie(Categorie):
    categorie_name = "Industrie"
    
class Alimentation(Categorie):
    categorie_name = "Alimentation"

CATEGORIES = [c.categorie_name for c in Categorie.__subclasses__()]