from Categorie import Industrie

class Dechetterie(Industrie):
    production_dechet_industriel = 0 # t/an
    consommation_energie = 0 # MWh/an
    consommation_eau = 0 # m3/an
    emission_co2 = 0 # t/an
    coefficient_co2 = 0 # Peu importe car emissions nulles

class PetiteEntreprise(Industrie):
    consommation_nourriture = 1095000 # kg/an
    traitement_dechet_industriel = 0 # t/an
    traitement_dechet_menager = 0 # t/an
    capacite_emploi = 3000 # personnes

class GrandeEntreprise(Industrie):
    consommation_nourriture = 1825000 # kg/an
    traitement_dechet_industriel = 0 # t/an
    traitement_dechet_menager = 0 # t/an
    capacite_emploi = 5000 # personnes



class BureauClassique(GrandeEntreprise):
    production_dechet_industriel = 0 # t/an
    consommation_energie = 6000 # MWh/an
    consommation_eau = 0 # m3/an
    emission_co2 = 428203 # kg/an
    coefficient_co2 = 2.5

class BureauIgh(GrandeEntreprise):
    production_dechet_industriel = 0 # t/an
    consommation_energie = 7500 # MWh/an
    consommation_eau = 0 # m3/an
    emission_co2 = 535254 # kg/an
    coefficient_co2 = 1.5

class PetiteDechetterieClassique(Dechetterie):
    consommation_nourriture = 5475 # kg/an
    traitement_dechet_industriel = 0 # t/an
    traitement_dechet_menager = 2906 # t/an
    capacite_emploi = 15 # personnes
    
class MoyenneDechetterieClassique(Dechetterie):
    consommation_nourriture = 8395 # kg/an
    traitement_dechet_industriel = 0 # t/an
    traitement_dechet_menager = 4359 # t/an
    capacite_emploi = 23 # personnes

class GrandeDechetterieClassique(Dechetterie):
    consommation_nourriture = 10950 # kg/an
    traitement_dechet_industriel = 0 # t/an
    traitement_dechet_menager = 7266 # t/an
    capacite_emploi = 30 # personnes

class PetiteDechetterieIndustrielle(Dechetterie):
    consommation_nourriture = 5475 # kg/an
    traitement_dechet_industriel = 80000 # t/an
    traitement_dechet_menager = 0 # t/an
    capacite_emploi = 15 # personnes
    
class MoyenneDechetterieIndustrielle(Dechetterie):
    consommation_nourriture = 8395 # kg/an
    traitement_dechet_industriel = 200000 # t/an
    traitement_dechet_menager = 0 # t/an
    capacite_emploi = 23 # personnes

class GrandeDechetterieIndustrielle(Dechetterie):
    consommation_nourriture = 10950 # kg/an
    traitement_dechet_industriel = 250000 # t/an
    traitement_dechet_menager = 0 # t/an
    capacite_emploi = 30 # personnes

class PmeTextile(GrandeEntreprise):
    production_dechet_industriel = 5632 # t/an
    consommation_energie = 12 # MWh/an
    consommation_eau = 58163 # m3/an
    emission_co2 = 856 # kg/an
    coefficient_co2 = 0.5

class PmeAutomobile(GrandeEntreprise):
    production_dechet_industriel = 4224 # t/an
    consommation_energie = 26 # MWh/an
    consommation_eau = 43623 # m3/an
    emission_co2 = 1856 # kg/an
    coefficient_co2 = 2

class PmeBtp(GrandeEntreprise):
    production_dechet_industriel = 147895 # t/an
    consommation_energie = 36 # MWh/an
    consommation_eau = 29082 # m3/an
    emission_co2 = 2569 # kg/an
    coefficient_co2 = 0.5
    
class PmeNouvelleTechnologie(GrandeEntreprise):
    production_dechet_industriel = 4224 # t/an
    consommation_energie = 1009 # MWh/an
    consommation_eau = 14541 # m3/an
    emission_co2 = 72009 # kg/an
    coefficient_co2 = 1.5


class GroupeTextile(GrandeEntreprise):
    production_dechet_industriel = 7743 # t/an
    consommation_energie = 24 # MWh/an
    consommation_eau = 118089 # m3/an
    emission_co2 = 1713 # kg/an
    coefficient_co2 = 0.5

class GroupeAutomobile(GrandeEntreprise):
    production_dechet_industriel = 5808 # t/an
    consommation_energie = 52 # MWh/an
    consommation_eau = 88567 # m3/an
    emission_co2 = 3711 # kg/an
    coefficient_co2 = 2

class GroupeBtp(GrandeEntreprise):
    production_dechet_industriel = 203355 # t/an
    consommation_energie = 71 # MWh/an
    consommation_eau = 59045 # m3/an
    emission_co2 = 5067 # kg/an
    coefficient_co2 = 0.5
    
class GroupeNouvelleTechnologie(GrandeEntreprise):
    production_dechet_industriel = 5808 # t/an
    consommation_energie = 1998 # MWh/an
    consommation_eau = 29522 # m3/an
    emission_co2 = 142592 # kg/an
    coefficient_co2 = 1.5
