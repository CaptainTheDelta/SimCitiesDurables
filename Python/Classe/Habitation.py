from Categorie import Habitation

class Residence(Habitation):
    production_dechet_menager = 2840 # t/an
    consommation_nourriture = 31025000 # kg/an
    consommation_eau = 250025 # m3/an
    capacite_hebergement = 5000 # personnes

class Immeuble(Habitation):
    production_dechet_menager = 5680 # t/an
    consommation_nourriture = 6205000 # kg/an
    consommation_eau = 500050 # m3/an
    capacite_hebergement = 10000 # personnes



class ResidenceBeton(Residence):
    consommation_energie = 18627 # MWh/an
    emission_co2 = 1329356 # kg/an
    coefficient_co2 = 0.5

class ResidenceMetallique(Residence):
    consommation_energie = 30818 # MWh/an
    emission_co2 = 2199393 # kg/an
    coefficient_co2 = 0.5

class ResidenceBiosource(Residence):
    consommation_energie = 17205 # MWh/an
    emission_co2 = 1227872 # kg/an
    coefficient_co2 = 2.5

class ResidenceRecycle(Residence):
    consommation_energie = 14923 # MWh/an
    emission_co2 = 1065012 # kg/an
    coefficient_co2 = 2.5

class ResidenceRehabitation(Residence):
    consommation_energie = 12909 # MWh/an
    emission_co2 = 921279 # kg/an
    coefficient_co2 = 2.5

class ImmeubleBeton(Immeuble):
    consommation_energie = 27576 # MWh/an
    emission_co2 = 1968021 # kg/an
    coefficient_co2 = 2.5

class ImmeubleMetallique(Immeuble):
    consommation_energie = 56212 # MWh/an
    emission_co2 = 4011690 # kg/an
    coefficient_co2 = 2.5

class ImmeubleBiosource(Immeuble):
    consommation_energie = 26182 # MWh/an
    emission_co2 = 1868535 # kg/an
    coefficient_co2 = 0.5

class ImmeubleRecycle(Immeuble):
    consommation_energie = 23944 # MWh/an
    emission_co2 = 1708815 # kg/an
    coefficient_co2 = 0.5

class ImmeubleRehabilitation(Immeuble):
    consommation_energie = 21970 # MWh/an
    emission_co2 = 1567936 # kg/an
    coefficient_co2 = 0.5