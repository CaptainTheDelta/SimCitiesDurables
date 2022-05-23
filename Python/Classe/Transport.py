from Categorie import Transport

class BusEssence(Transport):
    consommation_energie = 2102 # MWh/an
    consommation_nourriture = 109500 # kg/an
    capacite_emploi = 300 # personnes
    capacite_transport = 1200 # personnes
    emission_co2 = 150014 # kg/an
    coefficient_co2 = 0

class BusBioGnv(Transport):
    consommation_energie = 2102 # MWh/an
    consommation_nourriture = 109500 # kg/an
    capacite_emploi = 300 # personnes
    capacite_transport = 1200 # personnes
    emission_co2 = 30003 # kg/an
    coefficient_co2 = 2.5

class Tramway(Transport):
    consommation_energie = 18243 # MWh/an
    consommation_nourriture = 21900 # kg/an
    capacite_emploi = 60 # personnes
    capacite_transport = 35700 # personnes
    emission_co2 = 1301951 # kg/an
    coefficient_co2 = 2.5

class StationVelo(Transport):
    consommation_energie = 37 # MWh/an
    consommation_nourriture = 0 # kg/an
    capacite_emploi = 0 # personnes
    capacite_transport = 500 # personnes
    emission_co2 = 2641 # kg/an
    coefficient_co2 = 2.5

class VoitureElectrique(Transport):
    consommation_energie = 146 # MWh/an
    consommation_nourriture = 0 # kg/an
    capacite_emploi = 0 # personnes
    capacite_transport = 200 # personnes
    emission_co2 = 10420 # kg/an
    coefficient_co2 = 1.5

class VoitureThermique(Transport):
    consommation_energie = 3679 # MWh/an
    consommation_nourriture = 0 # kg/an
    capacite_emploi = 0 # personnes
    capacite_transport = 800 # personnes
    emission_co2 = 262560 # kg/an
    coefficient_co2 = 0