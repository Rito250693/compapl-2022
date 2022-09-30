#cadenas de formato
import os
os.system('cls')
ciudad0='zacatecas'
ciudad1='Guadalupe'
ciudad2='Fresnillo'

print('\n Salida con argumentos por posicion')
print('\n Posicion numerada en orden :{0} {1} {2}'.format(ciudad0, ciudad1, ciudad2))
print('\n posicion din numero        :{} {} {}'.format(ciudad0, ciudad1, ciudad2))
print('\n posicion numerada sin orden:{2} {1} {0}'.format(ciudad0, ciudad1, ciudad2))
print('\n Repetir Posisiciones:{2} {2} - {1} {1} - {0}'.format(ciudad0, ciudad1, ciudad2))

print('\n Argumentos por nombre: {x1} / {x2} / {x3}'.format(x1=5, x2=5*8, x3='jerez'))

txt='Maestria en Ingenieria y Tecnologia Aplicada'

print('\n Alinear texto y espesificar longitud\n')
print('{:*^60}'.format(txt))
print('{:<60}'.format(txt))
print('{:>60}'.format(txt))
print('{:^60}'.format(txt))

num=12345
print('\n\n Mostrar nueros en diferentes bases: ')
print('Decimal      0..9           : {:d}'.format(num))
print('Hexadecimal  0..9 ABCDEF    : {:X}'.format(num))
print('Hexadecimal  0..8           : {:o}'.format(num))
print('Hexadecimal  0,1            : {:b}'.format(num))

num  = 11123123131232234.56789
desc = 0.20
print('\n\nFormateo de datos\n')
print('Numero Decimal   : {:15}'.format(num))
print('Con Decimales    : {:.2f}'.format(num))
print('Relleno          : {:15.2f}'.format(num))
print('Exponencial      : {:e}'.format(num))
print('En porcentaje    : {:.2%}'.format(num))
print('Separand miles   : {:,.2f}'.format(num))