import os; os.system('cls')

print('cambiar los elementos de una lista\n')

nums=[10,9,8,5,6,8.8,7,5,6,2,9,5]

print(f'lista original    : {len(nums)} - {nums}')

nums[0]=7
nums[1]=7
print(f'cambiar 0 y 1     : {nums} \n')

nums[2:5] = [9,9,9]
print(f'cambiar del 2 al 4: {nums} \n')
