import os; os.system('cls')

print('acceder a los elementos de una lista')

nums=[10,20,30,40,60,70,10,20,99]

print(f'lista original             : {len(nums)} - {nums}\n')
print(f'primero y el ultimo        : {nums[0]} - {nums[8]}\n')
print(f'del 2 al 6                 : {nums[2:7]} \n')
print(f'los primeros 3             : {nums[:3]}\n')
print(f'los ultimos 3              :{nums[6:]} \n')
print(f'3 antes del ultimo         :{nums[5:8]} - {nums[-4:-1]} \n')
print(f'')