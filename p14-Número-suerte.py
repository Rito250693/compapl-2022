#Dado el año de nacimiento, la suma de sus dígitos individuales es el número de la suerte
import math
print('Se busca saber tu numero de la suerte')

año = int(input('Dame tu año de nacimiento'))

millares =math.trunc(año/1000)
centenas = math.trunc((año - (millares*1000))/100)
decenas =math.trunc( (año-(millares*1000 + centenas * 100))/10)
unidades = año -(millares *1000 + centenas * 100 + decenas *10)


print(f'millares {millares} centenas {centenas}, decenas {decenas}, unidades {unidades}')

numerosuerte = millares + centenas + decenas + unidades

print(f'el numero de la suerte es {numerosuerte}')