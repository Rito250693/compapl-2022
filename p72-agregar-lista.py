#agregar elemenotos a una lista existente
import os; os.system('cls')

print('agregar elemenotos a una lista existente')

nums= [80.3,12.5,60.2,30.4]
print(f' lista original   {len(nums)}  - {nums}')

nums.append(90)
nums.append(100)
print(f'agregar el 90 y el 100 al final      :  {nums}\n')
 
nums.insert(4,80)
print(f'insertar el 80 antes del 90          :  {nums}\n')

otros=[110,120,130]

nums.extend(otros)
print(f'extender la lista con 110 120 y 130  : {nums}\n')

nums.extend([5,6,7])
print(f'se agregaron otos 3 de forma directa : {nums}\n')

