#generar dos listas de numeros aleatorios

import random
import os; os.system('cls')

print('Generando lista de numeros aleatorios....')

l1=[]
l2=[]
l3=[]
for n in range(10):
    l1.append(random.randint(1,100))
    l2.append(random.randint(1,100))

print('\n listas de numeros originales')
print(f'lista1  : {l1}')
print(f'lista 2 : {l2}')

for n in range(10):
    l1[n]= pow(l1[n],2)
    l2[n]= pow(l2[n],2)
    l3.append( l1[n] + l2[n])

print('\n listas de numeros elevados')
print(f'lista 1 : {l1}')
print(f'lista 2 : {l2}')
print(f'lista 3 : {l3}')