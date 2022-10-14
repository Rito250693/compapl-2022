#capturar nombres y edades hasta introducir *
import os;os.system('cls')
nombres=[]
edades=[]

print('capturar nombres y edades hasta introducir *')
# introducir nombres y edades hasta que ingrese un asterisco
while True:
    nombre = input('nombre: ')
    if nombre=='*':
        break
    else:
        nombres.append(nombre)
        edad= int(input('Edad : '))
        edades.append(edad)
print('\n\n')
print(f'nombres: {len(nombres)} - {nombres}')
print(f'Edades : {len(edades)} - {edades}')

#recorrer el arreglo para ver los mayores de edad
for i in range(len(edades)):
    if edades[i] >=18:
        print(f'Nombre : {nombres[i]} - {edades[i]}')

#buscar el alumno de mayor edad
mayor = max(edades)
pos = edades.index(mayor)

print(f'El nombre del alumno con mayor edd es : {nombre[pos]} - {edades[pos]}')

