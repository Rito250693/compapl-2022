#trabajar con conjuntos

import os ; os.system('cls')

muns ={'Zacatecas','Guadalupe','Jerez','Fresnillo','Fresnillo'}

print(f'que tipo de variable es : {type(muns)}')
print(f'{len(muns)} - {muns}')

print(f'\n lista de municipios con ciclo for')
for m in muns:
    print(m,end=' ')

muns.add('Teul')
print(f'\n\nAgregar con add() a Teul : {muns} \n')

otros = {'Luis Moya','Ojocaliente','Tepetongo'}
muns.update(otros)
print(f'Agregar con update () Luis Moya, Ojocaliente, Tepetongo : \n {muns}\n')

muns.remove('Zacatecas')
print(f'Eliminar Zacatecas con Remove() : \n{muns}\n')

muns.discard('Ojocaliente')
print(f'eliminar con discard () a Ojocaliente : \n{muns}\n')

#eliminar el primer elemento del conjunto
muns.pop()
print(f'Eliminar con pop el primer elemento : \n{muns}\n -{m}')
