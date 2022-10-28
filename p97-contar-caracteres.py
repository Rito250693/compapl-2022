#Escribe un programa que lea una cadena y devuelva un diccionario con la cantidad de apariciones de cada carácter en la cadena.

cadena=input("Ingrese una palabra: ")
diccionario={}

for i in range(len(cadena)):
    diccionario[cadena[i]]=0

for d in diccionario.keys():
    cont=0

    for e in range(len(cadena)):
        if d==cadena[e]:
            cont+=1
            
    diccionario[d]=cont


print(f"{diccionario}")