from Categorie import Consommation

class CentreCommercialUrbain(Consommation):
    consommation_energie = 11250 # MWh/an
    consommation_nourriture = 82125 # kg/an
    capacite_emploi = 225 # personnes
    capacite_commerce = 20000 # personnes
    emission_co2 = 802880 # kg/an
    coefficient_co2 = 2.5

class CentreCommercialGrand(Consommation):
    consommation_energie = 22500 # MWh/an
    consommation_nourriture = 164250 # kg/an
    capacite_emploi = 450 # personnes
    capacite_commerce = 40000 # personnes
    emission_co2 = 1605761 # kg/an
    coefficient_co2 = 0.5

class CommerceProximitePetit(Consommation):
    consommation_energie = 771 # MWh/an
    consommation_nourriture = 27375 # kg/an
    capacite_emploi = 75 # personnes
    capacite_commerce = 5000 # personnes
    emission_co2 = 55024 # kg/an
    coefficient_co2 = 2.5

class CommerceProximiteGrand(Consommation):
    consommation_energie = 1550 # MWh/an
    consommation_nourriture = 54750 # kg/an
    capacite_emploi = 150 # personnes
    capacite_commerce = 10000 # personnes
    emission_co2 = 110619 # kg/an
    coefficient_co2 = 0.5