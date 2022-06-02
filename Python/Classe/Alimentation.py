from Categorie import Alimentation

class Agriculture(Alimentation):
    production_nourriture = 18524480 # kg/an
    production_dechet_industriel = 7317 # t/an
    consommation_nourriture = 4380 # kg/an
    consommation_eau = 0 # m3/an

class Culture(Alimentation):
    production_dechet_industriel = 0 # t/an
    consommation_eau = 1 # m3/an


class AgricultureIntensive(Agriculture):
    consommation_energie = 861 # MWh/an
    capacite_emploi = 12 # personnes
    emission_co2 = 61447 # t/an
    coefficient_co2 = 0.5

class AgricultureRaisonnee(Agriculture):
    consommation_energie = 865 # MWh/an
    capacite_emploi = 16 # personnes
    emission_co2 = 61733 # t/an
    coefficient_co2 = 1.5

class AgricultureBiologique(Agriculture):
    consommation_energie = 856 # MWh/an
    capacite_emploi = 20 # personnes
    emission_co2 = 61090 # t/an
    coefficient_co2 = 2.5

class PotagerTraditionnel(Culture):
    production_nourriture = 100000 # kg/an
    consommation_energie = 0 # MWh/an
    consommation_nourriture = 0 # kg/an
    capacite_emploi = 15 # personnes
    emission_co2 = 0 # t/an
    coefficient_co2 = 2.5

class FermeVerticale(Culture):
    production_nourriture = 2640000 # kg/an
    consommation_energie = 77000 # MWh/an
    consommation_nourriture = 7300 # kg/an
    capacite_emploi = 20 # personnes
    emission_co2 = 5495271 # t/an
    coefficient_co2 = 0.5

class ElevageIntensif(Culture):
    production_nourriture = 2690000 # kg/an
    consommation_energie = 9246 # MWh/an
    consommation_nourriture = 18250 # kg/an
    capacite_emploi = 50 # personnes
    emission_co2 = 659861 # t/an
    coefficient_co2 = 0.5

class ElevageExtensif(Culture):
    production_nourriture = 2690000 # kg/an
    consommation_energie = 6106 # MWh/an
    consommation_nourriture = 25550 # kg/an
    capacite_emploi = 70 # personnes
    emission_co2 = 435768 # t/an
    coefficient_co2 = 2.5
