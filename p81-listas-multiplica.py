#leer dos listas con 5 elementos 

import os;os.system('cls')

print('leer dos listas con 5 elementos y Multiplicarlas en una tercer lista')

print('\nleyendo lista 1 con 5 elementos ')
lista1=[]
for i in range(5) :
    n=int(input('Numero: '))
    lista1.append(n)
print('\nleyendo lista 2 con 5 elementos')
lista2=[]
for i in range(5):#aqui se le asigna el rango del cual se estaran recibiendo datos
    n=int(input('Numero: '))
    lista2.append(n)#aqui se señala que el la variable lista se le estara añadiendo lo que entre en n
lista3=[]
for i in range(5):
    lista3.append(lista1[i] * lista2[i])

print(f'lista 1 : {lista1}\n')

print(f'lista 2 : {lista2}')

print(f'lista 3 multiplicando la primera y la segunda\n        : {lista3}') 