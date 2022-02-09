""" Programa para apoyar al marinero Seijo
   

import utilidades as util

def probar_funciones():
  criatura= util.aparecer_criatura()
  direccion=util.aparecer_direccion()
  print(criatura, direccion)
  return criatura, direccion

#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================

# Ejecuta el programa varias veces para ver su funcionamiento

(animal, lugar)=probar_funciones()

if animal=="Kraken" or animal=="Hipocampo" or animal ==  "Pulpo":
  art = "un"
elif animal== "Ballena" or animal == "Macaraprono":
  art = "una"
elif animal == "Sirenas" or animal == "Hidras":
  art = "unas"
elif animal == "Leviatanes":
  art = "unos"

if lugar== "babor" or lugar == "estribor":
  art1 = "a"
elif lugar == "proa" or lugar == "popa":
  art1 = "por la " 

print("\n Seijo, atento debes gritar \n")
print (f"Ahoy! capitán, {art} {animal} {art1} {lugar}")



