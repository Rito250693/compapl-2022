#remover elementos de una lista existente
import os; os.system('cls')

print('Remover elementos de una lista Existente\n')

nums=[1,3,5,7,9,11,99,15,88,19,100]

print(f'lista completa                     : {len(nums)} - {nums}')

nums.remove(99)

print(f' Remover el 99 laprimera ocurrencia: {nums}')

num=nums.pop(8)#este es para eliminar un objeto de una posicion determinada 
print(f'remover elemento de una posicion 7 :{nums} - {num} \n')

num=nums.pop()#este es para eliminar un objeto de una posicion determinada 
print(f'remover el ultimo elemento         :{nums} - {num} \n')

nums.clear()
print(f'Remover todos                      : {nums}')