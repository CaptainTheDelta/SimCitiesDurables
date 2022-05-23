import openpyxl as xl
from .Categorie import *

excel = r"utils/res/plateau_excelV3.xlsx"
plateau_xl = xl.load_workbook(excel, data_only=True)
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
    def __init__(self, name, categorie, xl_data_line=1, xl_pollution_cell='A1'):
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

#============================ Production d'énergie ============================

class CentraleNucleaire(Bloc, ProductionEnergie):
    data = {}
    def __init__(self):
        super().__init__("centrale nucléaire", "Production d'énergie", 6, "F8")


class ParcEolien2(Bloc, ProductionEnergie):
    data = {}
    def __init__(self):
        super().__init__("parc éolien 2", "Production d'énergie", 7, "F9")


class ParcEolien5(Bloc, ProductionEnergie):
    data = {}
    def __init__(self):
        super().__init__("parc éolien 5", "Production d'énergie", 8, "F10")


class ParcEolien8(Bloc, ProductionEnergie):
    data = {}
    def __init__(self):
        super().__init__("parc éolien 8", "Production d'énergie", 9, "F11")


class CentraleCharbon(Bloc, ProductionEnergie):
    data = {}
    def __init__(self):
        super().__init__("centrale charbon", "Production d'énergie", 10, "F12")


class PanneauxSolaire400(Bloc, ProductionEnergie):
    data = {}
    def __init__(self):
        super().__init__("panneaux solaire 400", "Production d'énergie", 11, "F13")


class PanneauxSolaire1000(Bloc, ProductionEnergie):
    data = {}
    def __init__(self):
        super().__init__("panneaux solaire 1000", "Production d'énergie", 12, "F14")


class Barrage(Bloc, ProductionEnergie):
    data = {}
    def __init__(self):
        super().__init__("barrage", "Production d'énergie", 13, "F15")


class Raffinerie(Bloc, ProductionEnergie):
    data = {}
    def __init__(self):
        super().__init__("raffinerie", "Production d'énergie", 14, "F16")


class UniteMethanisation(Bloc, ProductionEnergie):
    data = {}
    def __init__(self):
        super().__init__("unité de méthanisation", "Production d'énergie", 15, "F17")


#================================= Habitation =================================

class ResidentielBeton(Bloc, Habitation):
    data = {}
    def __init__(self):
        super().__init__("résidentiel béton", "Habitation", 21, "H16")


class ResidentielMetallique(Bloc, Habitation):
    data = {}
    def __init__(self):
        super().__init__("résidentiel métallique", "Habitation", 22, "H17")


class ResidentielBiosource(Bloc, Habitation):
    data = {}
    def __init__(self):
        super().__init__("résidentiel biosourcé", "Habitation", 23, "H18")


class ResidentielRecycle(Bloc, Habitation):
    data = {}
    def __init__(self):
        super().__init__("résidentiel recyclé", "Habitation", 24, "H19")


class ResidentielRehabilitation(Bloc, Habitation):
    data = {}
    def __init__(self):
        super().__init__("résidentiel réhabilitation", "Habitation", 25, "H20")


class ImmeubleBeton(Bloc, Habitation):
    data = {}
    def __init__(self):
        super().__init__("immeuble béton", "Habitation", 26, "H21")


class ImmeubleMetallique(Bloc, Habitation):
    data = {}
    def __init__(self):
        super().__init__("immeuble métallique", "Habitation", 27, "H22")


class ImmeubleBiosource(Bloc, Habitation):
    data = {}
    def __init__(self):
        super().__init__("immeuble biosourcé", "Habitation", 28, "H23")


class ImmeubleRecycle(Bloc, Habitation):
    data = {}
    def __init__(self):
        super().__init__("immeuble recyclé", "Habitation", 29, "H24")


class ImmeubleRehabilitation(Bloc, Habitation):
    data = {}
    def __init__(self):
        super().__init__("immeuble réhabilitation", "Habitation", 30, "H25")


#=================================== Santé ====================================

class HopitalChu(Bloc, Sante):
    data = {}
    def __init__(self):
        super().__init__("hôpital CHU", "Santé", 36, "J27")


class HopitalClinique(Bloc, Sante):
    data = {}
    def __init__(self):
        super().__init__("hôpital clinique", "Santé", 37, "J28")


class MaisonRetraitePetit(Bloc, Sante):
    data = {}
    def __init__(self):
        super().__init__("maison de retraite petit", "Santé", 38, "J29")


class MaisonRetraiteGrand(Bloc, Sante):
    data = {}
    def __init__(self):
        super().__init__("maison de retraite grand", "Santé", 39, "J30")


#================================ Consommation ================================

class CentreCommercialUrbain(Bloc, Consommation):
    data = {}
    def __init__(self):
        super().__init__("centre commercial urbain", "Consommation", 45, "L32")


class CentreCommercialGrande(Bloc, Consommation):
    data = {}
    def __init__(self):
        super().__init__("centre commercial grande", "Consommation", 46, "L33")


class GroupementCommercesProximitePetit(Bloc, Consommation):
    data = {}
    def __init__(self):
        super().__init__("groupement de commerces de proximité petit", "Consommation", 47, "L34")


class GroupementCommercesProximiteGrand(Bloc, Consommation):
    data = {}
    def __init__(self):
        super().__init__("groupement de commerces de proximité grand", "Consommation", 48, "L35")


#==================================== Eau =====================================

class StationEpuration100(Bloc, Eau):
    data = {}
    def __init__(self):
        super().__init__("station épuration 100", "Eau", 54, "N37")


class StationEpuration150(Bloc, Eau):
    data = {}
    def __init__(self):
        super().__init__("station épuration 150", "Eau", 55, "N38")


class StationEpuration200(Bloc, Eau):
    data = {}
    def __init__(self):
        super().__init__("station épuration 200", "Eau", 56, "N39")


class StationEauPotable100(Bloc, Eau):
    data = {}
    def __init__(self):
        super().__init__("station eau potable 100", "Eau", 57, "N40")


class StationEauPotable150(Bloc, Eau):
    data = {}
    def __init__(self):
        super().__init__("station eau potable 150", "Eau", 58, "N41")


class StationEauPotable200(Bloc, Eau):
    data = {}
    def __init__(self):
        super().__init__("station eau potable 200", "Eau", 59, "N42")


#================================= Education ==================================

class GroupeScolaire(Bloc, Education):
    data = {}
    def __init__(self):
        super().__init__("groupe scolaire", "Education", 65, "O37")


class Universite(Bloc, Education):
    data = {}
    def __init__(self):
        super().__init__("université", "Education", 66, "O38")


#================================= Transports =================================

class BusEssence(Bloc, Transport):
    data = {}
    def __init__(self):
        super().__init__("bus  essence", "Transports", 72, "P47")


class BusBiognv(Bloc, Transport):
    data = {}
    def __init__(self):
        super().__init__("bus  bioGNV", "Transports", 73, "P48")


class Tramway(Bloc, Transport):
    data = {}
    def __init__(self):
        super().__init__("tramway", "Transports", 74, "P49")


class StationVelo(Bloc, Transport):
    data = {}
    def __init__(self):
        super().__init__("station de vélo", "Transports", 75, "P50")


class VoitureElectriques(Bloc, Transport):
    data = {}
    def __init__(self):
        super().__init__("voiture électriques", "Transports", 76, "P51")


class VoitureThermiques(Bloc, Transport):
    data = {}
    def __init__(self):
        super().__init__("voiture thermiques", "Transports", 77, "P52")


#================================= Industrie ==================================

class BureauClassique(Bloc, Industrie):
    data = {}
    def __init__(self):
        super().__init__("bureau classique", "Industrie", 83, "R54")


class BureauIgh(Bloc, Industrie):
    data = {}
    def __init__(self):
        super().__init__("bureau IGH", "Industrie", 84, "R55")


class DechetterieClassiquePetite(Bloc, Industrie):
    data = {}
    def __init__(self):
        super().__init__("déchetterie classique petite", "Industrie", 85, "R56")


class DechetterieClassiqueMoyenne(Bloc, Industrie):
    data = {}
    def __init__(self):
        super().__init__("déchetterie classique moyenne", "Industrie", 86, "R57")


class DechetterieClassiqueGrande(Bloc, Industrie):
    data = {}
    def __init__(self):
        super().__init__("déchetterie classique grande", "Industrie", 87, "R58")


class DechetterieIndutriellePetite(Bloc, Industrie):
    data = {}
    def __init__(self):
        super().__init__("déchetterie indutrielle petite", "Industrie", 88, "R59")


class DechetterieIndutrielleMoyenne(Bloc, Industrie):
    data = {}
    def __init__(self):
        super().__init__("déchetterie indutrielle moyenne", "Industrie", 89, "R60")


class DechetterieIndutrielleGrande(Bloc, Industrie):
    data = {}
    def __init__(self):
        super().__init__("déchetterie indutrielle grande", "Industrie", 90, "R61")


class TpePmeTextile(Bloc, Industrie):
    data = {}
    def __init__(self):
        super().__init__("TPE/PME textile", "Industrie", 91, "R62")


class TpePmeAutomobile(Bloc, Industrie):
    data = {}
    def __init__(self):
        super().__init__("TPE/PME automobile", "Industrie", 92, "R63")


class TpePmeBtp(Bloc, Industrie):
    data = {}
    def __init__(self):
        super().__init__("TPE/PME BTP", "Industrie", 93, "R64")


class TpePmeNouvelleTechnologie(Bloc, Industrie):
    data = {}
    def __init__(self):
        super().__init__("TPE/PME nouvelle technologie", "Industrie", 94, "R65")


class GroupeTextile(Bloc, Industrie):
    data = {}
    def __init__(self):
        super().__init__("groupe textile", "Industrie", 95, "R66")


class GroupeAutomobile(Bloc, Industrie):
    data = {}
    def __init__(self):
        super().__init__("groupe automobile", "Industrie", 96, "R67")


class GroupeBtp(Bloc, Industrie):
    data = {}
    def __init__(self):
        super().__init__("groupe BTP", "Industrie", 97, "R68")


class GroupeNouvelleTechnologie(Bloc, Industrie):
    data = {}
    def __init__(self):
        super().__init__("groupe nouvelle technologie", "Industrie", 98, "R69")


#================================ Alimentation ================================

class AgricultureIntensif(Bloc, Alimentation):
    data = {}
    def __init__(self):
        super().__init__("agriculture intensif", "Alimentation", 104, "T71")


class AgricultureRaisonnee(Bloc, Alimentation):
    data = {}
    def __init__(self):
        super().__init__("agriculture raisonnée", "Alimentation", 105, "T72")


class AgricultureBiologique(Bloc, Alimentation):
    data = {}
    def __init__(self):
        super().__init__("agriculture biologique", "Alimentation", 106, "T73")


class PotagerPotager(Bloc, Alimentation):
    data = {}
    def __init__(self):
        super().__init__("potager potager", "Alimentation", 107, "T74")


class PotagerFerme(Bloc, Alimentation):
    data = {}
    def __init__(self):
        super().__init__("potager ferme", "Alimentation", 108, "T75")


class ElevageIntensif(Bloc, Alimentation):
    data = {}
    def __init__(self):
        super().__init__("élevage intensif", "Alimentation", 109, "T76")


class ElevageExtensif(Bloc, Alimentation):
    data = {}
    def __init__(self):
        super().__init__("élevage extensif", "Alimentation", 110, "T77")


