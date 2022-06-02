from Categorie import ProductionEnergie

class CentraleNucleaire(ProductionEnergie):
    production_electricite = 6000000 # Wh/an
    production_dechet_industriel = 234 # t/an
    consommation_nourriture = 730000 # kg/an
    consommation_eau = 1095 # m3/an
    consommation_dechet_industriel = 0 # t/an
    capacite_emploi = 2000 # personnes
    emission_co2 = 396000000 # kg/an
    coefficient_co2 = 0

class CentraleCharbon(ProductionEnergie):
    production_electricite = 3700000 # Wh/an
    production_dechet_industriel = 703 # t/an
    consommation_nourriture = 11100000 # kg/an
    consommation_eau = 1095 # m3/an
    consommation_dechet = 0 # t/an
    capacite_emploi = 200 # personnes
    emission_co2 = 396000000 # kg/an
    coefficient_co2 = 0

class Eolienne2(ProductionEnergie):
    production_electricite = 176000 # Wh/an
    production_dechet_industriel = 0 # t/an
    consommation_nourriture = 0 # kg/an
    consommation_eau = 0 # m3/an
    consommation_dechet = 0 # t/an
    capacite_emploi = 0 # personnes
    emission_co2 = 2235200 # kg/an
    coefficient_co2 = 2.5

class Eolienne5(ProductionEnergie):
    production_electricite = 400000 # Wh/an
    production_dechet_industriel = 0 # t/an
    consommation_nourriture = 0 # kg/an
    consommation_eau = 0 # m3/an
    consommation_dechet = 0 # t/an
    capacite_emploi = 0 # personnes
    emission_co2 = 6060000 # kg/an
    coefficient_co2 = 2.5

class Eolienne8(ProductionEnergie):
    production_electricite = 720000 # Wh/an
    production_dechet_industriel = 0 # t/an
    consommation_nourriture = 0 # kg/an
    consommation_eau = 0 # m3/an
    consommation_dechet = 0 # t/an
    capacite_emploi = 0 # personnes
    emission_co2 = 13176000 # kg/an
    coefficient_co2 = 2.5

class PanneauSolaire400(ProductionEnergie):
    production_electricite = 37 # Wh/an
    production_dechet_industriel = 77 # t/an
    consommation_nourriture = 0 # kg/an
    consommation_eau = 0 # m3/an
    consommation_dechet = 0 # t/an
    capacite_emploi = 0 # personnes
    emission_co2 = 2072 # kg/an
    coefficient_co2 = 2.5

class PanneauSolaire1000(ProductionEnergie):
    production_electricite = 93 # Wh/an
    production_dechet_industriel = 157 # t/an
    consommation_nourriture = 0 # kg/an
    consommation_eau = 0 # m3/an
    consommation_dechet = 0 # t/an
    capacite_emploi = 0 # personnes
    emission_co2 = 7812 # kg/an
    coefficient_co2 = 2.5

class Barrage(ProductionEnergie):
    production_electricite = 15000 # Wh/an
    production_dechet_industriel = 0 # t/an
    consommation_nourriture = 14600 # kg/an
    consommation_eau = 0 # m3/an
    consommation_dechet = 0 # t/an
    capacite_emploi = 40 # personnes
    emission_co2 = 195000 # kg/an
    coefficient_co2 = 2.5

class Raffinerie(ProductionEnergie):
    production_electricite = 186080000 # Wh/an
    production_dechet_industriel = 1172 # t/an
    consommation_nourriture = 237250 # kg/an
    consommation_eau = 12800000 # m3/an
    consommation_dechet = 0 # t/an
    capacite_emploi = 6500 # personnes
    emission_co2 = 144770240000 # kg/an
    coefficient_co2 = 0

class UniteMethanisation(ProductionEnergie):
    production_electricite = 20000 # Wh/an
    production_dechet_industriel = 0 # t/an
    consommation_nourriture = 64 # kg/an
    consommation_eau = 0 # m3/an
    consommation_dechet = 14000 # t/an
    capacite_emploi = 14 # personnes
    emission_co2 = 320000 # kg/an
    coefficient_co2 = 0