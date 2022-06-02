batiment = [ [] for _ in range (9) ]
# contient la liste des batiments poses par categorie

def pollution (batiment):
   c_point = 0
   bat = batiment[0 : 5]+batiment[6 : 9]
   for categorie in bat:
     # il y a 9 categories mais l_education ne pollue pas (postulat)
     numerateur = 0
     denominateur = 0
     for bloc in categorie:
         numerateur += bloc.consommation_co2()*bloc.coefficient_co2()
         denominateur += bloc.consommation_co2()
     c_point += numerateur/denominateur
   return c_point
