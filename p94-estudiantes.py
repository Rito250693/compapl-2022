#lista conformada o integrada donde cada elemento[10][20][30][40]
import os;os.system('cls')
grupo=[
    {'nombre':'Carlos','edad':45,'carrera':'Sistemas','promedio':9},
    {'nombre':'Rocio','edad':35,'carrera':'Quimica','promedio':10}
]

print(f'Grupo inicial : \n {len(grupo)} - {grupo}')

n = int(input('cuantos Estudiantes deseas procesar ? '))

for i in range(n):
    datos={}
    datos['nombre']   = input('nombre')
    datos['Edad']     = int(input('edad'))
    datos['Carrera']  = input('carrera')
    datos['promedio'] = float(input('promedio'))
    grupo.append(datos)

print(f'grupo final : \n {len(grupo)} - {grupo}\n\n')

for e in grupo:
    for dato, valor in e.items():
        print(f'{dato:<10} : {valor}')
        print('')