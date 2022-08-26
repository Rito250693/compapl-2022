#dividir un numero de tres cifras en centenas decenas y unidades
#452 4 2 5

import math

print('dividir un numero de tres cifras, encentenas, decenas y unidades')

num = int(input('dame un numero entero de 3 cifras'))

centenas = math.trunc(num / 100)
decenas =math.trunc( (num -centenas * 100)/10)
unidades =num -(centenas * 100 + decenas *10)

print(f'centenas {centenas}, decenas {decenas}, unidades {unidades}')