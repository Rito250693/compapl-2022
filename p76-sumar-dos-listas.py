#leer dos listas de n numeros y sumarlas en una tercer lista

import os;os.system('cls')

print('leer dos listas de n numeros y sumarlas en una tercer lista')

c=int(input('cuantos elementos ? '))

#leer lista 1
print('\nleyendo lista 1')
lista1=[]
for i in range(c):
    n=int(input('Numero: '))
    lista1.append(n)
print(f'lista 1 :   {len(lista1)} - {lista1}')

#leer la lista 2
print('\nleyendo lista 2')
lista2=[]
for i in range(c):
    n=int(input('Numero: '))
    lista2.append(n)
print(f'lista 1 :   {len(lista2)} - {lista2}')

#sumar lista 3= lista 1 + lista 2
lista3=[]
for i in range(c):
    lista3.append(lista1[i]+lista2[i])

print(f'lista 3 :   {len(lista3)} - {lista3}')