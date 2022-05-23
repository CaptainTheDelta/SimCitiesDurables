from Categorie import Sante

class Chu(Sante):
    consommation_energie = 27000 # MWh/an
    consommation_nourriture = 1558550 # kg/an
    consommation_eau = 55006 # m3/an
    capacite_hebergement = 0 # personnes
    capacite_formation = 250 # personnes
    capacite_emploi = 1300 # personnes
    capacite_soin_hopital = 1100 # personnes
    capacite_soin_ehpad = 0 # personnes
    emission_co2 = 1926913 # kg/an
    coefficient_co2 = 2.5

class Clinique(Sante):
    consommation_energie = 13500 # MWh/an
    consommation_nourriture = 779275 # kg/an
    consommation_eau = 27503 # m3/an
    capacite_hebergement = 0 # personnes
    capacite_formation = 0 # personnes
    capacite_emploi = 650 # personnes
    capacite_soin_hopital = 550 # personnes
    capacite_soin_ehpad = 0 # personnes
    emission_co2 = 1926913 # kg/an
    coefficient_co2 = 1.5

class PetitEhpad(Sante):
    consommation_energie = 3000 # MWh/an
    consommation_nourriture = 368650 # kg/an
    consommation_eau = 15002 # m3/an
    capacite_hebergement = 300 # personnes
    capacite_formation = 0 # personnes
    capacite_emploi = 200 # personnes
    capacite_soin_hopital = 0 # personnes
    capacite_soin_ehpad = 300 # personnes
    emission_co2 = 214101 # kg/an
    coefficient_co2 = 2.5

class GrandEhpad(Sante):
    consommation_energie = 6000 # MWh/an
    consommation_nourriture = 737300 # kg/an
    consommation_eau = 30004 # m3/an
    capacite_hebergement = 600 # personnes
    capacite_formation = 0 # personnes
    capacite_emploi = 400 # personnes
    capacite_soin_hopital = 0 # personnes
    capacite_soin_ehpad = 600 # personnes
    emission_co2 = 428203 # kg/an
    coefficient_co2 = 1.5
