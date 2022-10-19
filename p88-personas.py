import os;os.system('cls')

a={'Juan','Maria','Pedro','Jose','Rocio'}
b={'Pedro','Juan','Pablo','Mateo','Esther',}

print(f'dados los diguientes nombres')
print(a)
print(f'{b}\n')
print('union de conjuntos')
print(f'A union B                : {a | b}\n')

print('interseccion de conjuntos')
print(f'A interseccion de B      : {a & b} \n ')

print('diferencia de los conjuntos')
print(f'A diferencia de B        : {a - b} \n')

print('Diferencia simetrica de conjuntos')
print(f'A diferencia simetrica B : {a ^ b}\n')

print('\nsi el conjunto de pablo y mateo es subconjunto de b ')
if 'Pablo' and 'Mateo' in b:
    print('Pablo y Mateo son  subconjunto de B')
else:
    print('no son subconjuntos')

print('\nsi el conjunto A, es superconjuno de nombres Reynaldo y Angelica')
if 'Reynaldo' and 'Angelica' in a:
    print('A es superconjunto de los conjuntos Reynaldo y Angelica')
else:
    print('A no es Superconjunto de los conjuntos Reynaldo y Angelica')

print('\nSi pedro esta en A\n')
if 'Pedro' in a:
    print('Pedro esta en A')
else:
    print('Pedro no esta en A')

print('\nSi Lilia no esta en B\n')
if 'Lilia' in b:
    print('lilia esta en B')
else:
    print('Lilia no esta en B')