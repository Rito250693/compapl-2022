#calsegunda ley de newton fuerza =masa * aceleracion

from re import A


print('calculando los valores de la segunda ley de newton\n')
print('[F] fuerza f = m * a')
print('[M Masa     m = f/a ')
print('[A] celeracion a = f / m')

op = str.upper(input('eige una opcion  '))

if op=='F':
    print('calculando la fuerza')
    m =int(input('dame la masa'))
    a = int(input('dame la aceleracion'))
    f= m * a
    print(f'la fuerza es {f}')
elif op =='M':
    print('calculando la masa')
    f = int(input('dame la fuerza'))
    a = int(input('dame la aceleracion'))
    m = f / a 
    print(f'la masa es {m}')
elif op == 'a':
    print('calculando la aceleracion')
    f = int(input('dame la duerza'))
    m = int(input('dame la masa'))
    a = f / m
    print(f'la aceleracion es {a}')
else:
    print('la opcion es incorrecta')
print('gracias por utilizar mi programa')