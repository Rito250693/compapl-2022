#El usuario introduce dos palabras con igual número de letras y combinarlas 

import os ; os.system('cls')

print('El usuario introduce dos palabras con igual número de letras y combinarlas\n ')
p1=input("Ingrese una palabra : ")
p2=input("Ingrese otra palabra: ")
c=""

if len(p1)==len(p2):
    for i in range(len(p1)):
        c+=p1[i]
        c+=p2[i]
    print(f"Palabra 1 : {p1}")
    print(f"Palabra 2 : {p2}")
    print(f"Combinadas: {c}")

else:
    print("Las palabras son de distinto tamaño!!")
    print(f"    La palabra {p1} tien {len(p1)} caracteres.")
    print(f"    La palabra {p2} tien {len(p2)} caracteres.")