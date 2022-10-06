#iterar sobre los elementos de la lista
import os; os.system('cls')

print(f'iterar sobre los elementos de la lista')

nums=[2,4,6,8,10,12,14,16]

print(f'Lista original: {len(nums)} - {nums}\n')
 
print('\npuedo yo pasar o iterar por los elementos de la lista:')

for n in nums:
    print(n)
print('\niterar por los elementos dela lista en bace al indice')

for n in range(len(nums)):
    print(nums[n])

print('\n sumar 2 a cada elemento de la lista:')
for n in nums:
    n=n+2
    print(n+2)
print(f'lista modificada      :     {nums}')

print('\niterar por los elementos de la lista afectandola')

for n in range(len(nums)):
    nums[n]=nums[n]+2
print(f'lista modificada: {nums}')
