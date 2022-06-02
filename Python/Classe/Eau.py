from Categorie import Eau

class StationEpuration100(Eau):
    production_eau = 0 # m3/an
    production_dechet_industriel = 2906 # t/an
    consommation_energie = 2520 # MWh/an
    consommation_nourriture = 1825 # kg/an
    traitement_eau = 2832636 # m3/an
    capacite_emploi = 5 # personnes
    emission_co2 = 179845 # kg/an
    coefficient_co2 = 2.5

class StationEpuration150(Eau):
    production_eau = 0 # m3/an
    production_dechet_industriel = 4359 # t/an
    consommation_energie = 3360 # MWh/an
    consommation_nourriture = 2433 # kg/an
    traitement_eau = 3776848 # m3/an
    capacite_emploi = 7 # personnes
    emission_co2 = 239794 # kg/an
    coefficient_co2 = 1.5

class StationEpuration200(Eau):
    production_eau = 0 # m3/an
    production_dechet_industriel = 7266 # t/an
    consommation_energie = 5040 # MWh/an
    consommation_nourriture = 3650 # kg/an
    traitement_eau = 5665272 # m3/an
    capacite_emploi = 10 # personnes
    emission_co2 = 359690 # kg/an
    coefficient_co2 = 0.5

class StationEauPotable100(Eau):
    production_eau = 3147374 # m3/an
    production_dechet_industriel = 0 # t/an
    consommation_energie = 1763 # MWh/an
    consommation_nourriture = 730 # kg/an
    traitement_eau = 0 # m3/an
    capacite_emploi = 3 # personnes
    emission_co2 = 125820 # kg/an
    coefficient_co2 = 2.5

class StationEauPotable150(Eau):
    production_eau = 4196498 # m3/an
    production_dechet_industriel = 0 # t/an
    consommation_energie = 2350 # MWh/an
    consommation_nourriture = 973 # kg/an
    traitement_eau = 0 # m3/an
    capacite_emploi = 3 # personnes
    emission_co2 = 167713 # kg/an
    coefficient_co2 = 1.5

class StationEauPotable200(Eau):
    production_eau = 6294747 # m3/an
    production_dechet_industriel = 0 # t/an
    consommation_energie = 3525 # MWh/an
    consommation_nourriture = 1460 # kg/an
    traitement_eau = 0 # m3/an
    capacite_emploi = 4 # personnes
    emission_co2 = 251569 # kg/an
    coefficient_co2 = 0.5