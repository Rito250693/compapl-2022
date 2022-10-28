#el usuario introduce nombres y edades, calcula y muestra la suma y promedio de edades
import os;os.system('cls')

datos={}
print('Introduce nombre y edad {nombre bacio para terminar}')

while True:
    nombre=input('Dame el nombre ? ')
    if nombre!='':
        edad = int(input('Dame la edad ? '))
        datos[nombre]= edad
    else:
        break

print(f'\nlos datos son :\n {len(datos)} - {datos}')

s=p=0
for n,e in datos.items():
    print(f'{n:<15} - {e:2}')
    s=s+e
p=s/len(datos)

print(f'\n\nLa suma :{s}\n el Promedio : {p}')