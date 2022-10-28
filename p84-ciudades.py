#leer nombres de n ciudades hasta ntroducir $
import os;os.system('cls')
nombres=[]

nombre=""

print("Ingrese el nombre de ciudades poner $ para terminar")

while True:
    nombre=input()
    if nombre!='$':
        nombres.append(nombre)
    else:
        break

print(f"Son {len(nombres)} ciudades - {nombres}")

nombres.sort(reverse=True)

print(f"La lista ordenada de forma descendente: {nombres}")

ciudades=[]

for c in nombres:
    if not c[0] in "aeiouAEIOU":
        ciudades.append(c)


print(f"Las ciudades que comienzan con consonante son {len(ciudades)} - {ciudades}")