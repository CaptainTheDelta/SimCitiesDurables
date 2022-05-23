# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
class Bloc():
    ordre = None

    def __init__(self, abscisse, ordonnee):
        self.x = abscisse
        self.y = ordonnee
    def coordonnee(self):
        return (self.x, self.y)

class ProductionEnergie(Bloc):
    ordre = 0
    production_nourriture = 0 # kg/an
    production_eau = 0 # m3/an
    production_dechet_menager = 0 # t/an
    consommation_energie = 0 # MWh/an
    traitement_eau = 0 # m3/an
    traitement_dechet_industriel = 0 # t/an
    traitement_dechet_menager = 0 # t/an
    capacite_emploi = 0 # personnes

class Habitation(Bloc):
    ordre = 1
    production_electricite = 0 # Mwh/an
    production_nourriture = 0 # kg/an
    production_eau = 0 # m3/an
    production_dechet_industriel = 0 # t/an
    consommation_dechet = 0 # t/an
    traitement_eau = 0 # m3/an
    traitement_dechet_industriel = 0 # t/an
    traitement_dechet_menager = 0 # t/an
    capacite_hebergement = 0 # personnes
    
class Sante(Bloc):
    ordre = 2
    production_electricite = 0 # Mwh/an
    production_nourriture = 0 # kg/an
    production_eau = 0 # m3/an
    production_dechet_industriel = 0 # t/an
    production_dechet_menager = 0 # t/an
    consommation_dechet = 0 # t/an
    traitement_eau = 0 # m3/an
    traitement_dechet_industriel = 0 # t/an
    traitement_dechet_menager = 0 # t/an
    capacite_transport = 0 # personnes
    capacite_commerce = 0 # personnes
    
class Consommation(Bloc):
    ordre = 3
    production_electricite = 0 # Mwh/an
    production_nourriture = 0 # kg/an
    production_eau = 0 # m3/an
    production_dechet_industriel = 0 # t/an
    production_dechet_menager = 0 # t/an
    consommation_eau = 0 # m3/an
    consommation_dechet = 0 # t/an
    traitement_eau = 0 # m3/an
    traitement_dechet_industriel = 0 # t/an
    traitement_dechet_menager = 0 # t/an
    capacite_hebergement = 0 # personnes
    capacite_formation = 0 # personnes
    capacite_transport = 0 # personnes
    capacite_soin_hopital = 0 # personnes
    capacite_soin_ehpad = 0 # personnes

class Eau(Bloc):
    ordre = 4
    production_electricite = 0 # Mwh/an
    production_nourriture = 0 # kg/an
    production_dechet_menager = 0 # t/an
    consommation_eau = 0 # m3/an
    consommation_dechet = 0 # t/an
    traitement_eau = 0 # m3/an
    traitement_dechet_industriel = 0 # t/an
    traitement_dechet_menager = 0 # t/an
    capacite_hebergement = 0 # personnes
    capacite_formation = 0 # personnes
    capacite_transport = 0 # personnes
    capacite_soin_hopital = 0 # personnes
    capacite_soin_ehpad = 0 # personnes
    capacite_commerce = 0 # personnes

class Education(Bloc) :
    ordre = 5
    production_electricite = 0 # Mwh/an
    production_nourriture = 0 # kg/an
    production_eau = 0 # m3/an
    production_dechet_industriel = 0 # t/an
    production_dechet_menager = 0 # t/an
    consommation_eau = 0 # m3/an
    consommation_dechet = 0 # t/an
    traitement_eau = 0 # m3/an
    traitement_dechet_industriel = 0 # t/an
    traitement_dechet_menager = 0 # t/an
    capacite_hebergement = 0 # personnes
    capacite_transport = 0 # personnes
    capacite_soin_hopital = 0 # personnes
    capacite_soin_ehpad = 0 # personnes
    capacite_commerce = 0 # personnes
    emission_co2 = 0 # kg/an
    coefficient_co2 = 0

class Transport(Bloc):
    ordre = 6
    production_electricite = 0 # Mwh/an
    production_nourriture = 0 # kg/an
    production_eau = 0 # m3/an
    production_dechet_industriel = 0 # t/an
    production_dechet_menager = 0 # t/an
    consommation_eau = 0 # m3/an
    consommation_dechet = 0 # t/an
    traitement_eau = 0 # m3/an
    traitement_dechet_industriel = 0 # t/an
    traitement_dechet_menager = 0 # t/an
    capacite_hebergement = 0 # personnes
    capacite_formation = 0 # personnes
    capacite_soin_hopital = 0 # personnes
    capacite_soin_ehpad = 0 # personnes
    capacite_commerce = 0 # personnes
    
class Industrie(Bloc):
    ordre = 7
    production_electricite = 0 # Mwh/an
    production_nourriture = 0 # kg/an
    production_eau = 0 # m3/an
    production_dechet_menager = 0 # t/an
    consommation_dechet = 0 # t/an
    traitement_eau = 0 # m3/an
    capacite_hebergement = 0 # personnes
    capacite_formation = 0 # personnes
    capacite_transport = 0 # personnes
    capacite_soin_hopital = 0 # personnes
    capacite_soin_ehpad = 0 # personnes
    capacite_commerce = 0 # personnes
    
class Alimentation(Bloc):
    ordre = 8
    production_electricite = 0 # Mwh/an
    production_eau = 0 # m3/an
    production_dechet_menager = 0 # t/an
    consommation_dechet = 0 # t/an
    traitement_eau = 0 # m3/an
    traitement_dechet_industriel = 0 # t/an
    traitement_dechet_menager = 0 # t/an
    capacite_hebergement = 0 # personnes
    capacite_formation = 0 # personnes
    capacite_transport = 0 # personnes
    capacite_soin_hopital = 0 # personnes
    capacite_soin_ehpad = 0 # personnes
    capacite_commerce = 0 # personnes