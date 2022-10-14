#operaciones bacicas de conjuntos

import os ; os.system('cls')

c1={1,2,3,4,5}
c2={5,6,7,8,9,10}
c3={9,10,11,12,13}
c4={3,4,5}

print(f'c1: {c1}\n c2: {c2}\n c3: {c3} c4: {c4}')

print('\n Union')
print(f'c1 union c2: {c1.union(c2)}')
print(f'c1 union c3: {c1 | c3}')

print('\nInterseccion:   ')
print(f'c1 interseccion c2: {c1.intersection(c2)}')
print(f'c2 interseccion c3: {c2 & c3}')

print('\n Diferencia')
print(f'c1 Diferencia c4: {c1.difference(c4)}')
print(f'c2 diferencia c3: {c2 - c3}')

print('\n Diferencia simetrica')
print(f'c1 dif dimetrica c2: {c1.symmetric_difference(c2)}')
print(f'c2 dif simetrica c3: {c2 ^ c3}')

print('\n Probar superconjuntos')
print(f'c1 es papa de c4: {c1.issubset(c4)}')
print(f'c2 es papa de c3: {c2>=c3}')

print('\n Probar Subconjuntos')
print(f'c4 es subconjunto de c1: {c4.issubset(c1)}')
print(f'c3 es hijo de c2: {c3<=c2}')

print('\n probar si un elemento esta o no en un conjunto ')
print(f'2 esta en c1: {2 in c1}')
print(f'6 no esta en c2: {6 not in c2}')