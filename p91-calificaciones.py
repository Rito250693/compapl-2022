#crear un diccionario de materias y calificaciones en base a dos listas 
import os;os.system('cls')

materias=['Fisica','Quimica','Matematicas','Geografia','Estadistica']
califs=[10,9,8,7.5,6]
print(f'lista de materias       : \n{materias}')
print(f'Lista de Calificaciones : \n{califs}')

notas=dict(zip(materias,califs))

print(f'Diccionario de notas:  \n {len (notas)} - {notas}')

notas.update({'ingles':10})
notas.update({'programacion':7})
print(f'Se agregaron elementos : \n {len(notas)} - {notas}')

notas.update({'Quimica':10})
notas['Matematicas']=10
print(f'Se agregaron elementos : \n {len(notas)} - {notas}')

print('\n listado de materias y calificaciones')
s=prom=0
for m,c in notas.items():
    print(f'{m:<12} - {c:5}')
    s=s+c
prom= s/len(notas)

print(f'la suma  {s:.2f}, promedio {prom:.2f}')

notas.clear()
print(f'Se borro Todo\n {len(notas)} - {notas}')