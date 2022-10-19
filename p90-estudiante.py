#diccionario con los datos de un estudiante
import os ; os.system('cls')

estudiante={
    'nombre':'juan Perez',
    'edad':45,
    'correo':'jperez@msn.com',
    'carrera':'sistemas'
}

print(f'El diccionario : \n{len(estudiante)} - {estudiante}')

estudiante['calificacion ']=9.5
estudiante['correo']='jperez@gmail.com'

print(f'El diccionario actualizado: \n {len(estudiante)} - {estudiante}')

estudiante.popitem()#este elimina la ultima entrada 

print(f'las llaves :\n {estudiante.keys()}\n')
for k in estudiante.keys():
    print(k)

print(f'los valores: \n{estudiante.values()}\n')
for v in estudiante.values():
    print(v)

print('\n llaves y valores : \n')
for k,v in estudiante.items():
    print(f'{k:<14} : {v}')
