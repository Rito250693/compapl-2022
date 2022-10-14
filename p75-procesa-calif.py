# procesar n calificaciones introducidas por el usuario

import os; os.system('cls')

print('procesar n calificaciones introducidas por el usuario')
print('introduce calificaciones de 0...10, usa 99 para parar\n')

n=0
nums=[]
suma=prom=0

while n!=99:
    n=int(input('Numero > '))
    if n>=0 and n<=10:
        nums.append(n)
        suma=suma+n
    else:
        print('X')

prom= suma / len(nums)

mp=[]   
for num in nums:
    if num>prom:
        mp.append(num)

print(f'Calificaciones      : {len(nums)} - {nums}')
print(f'La suma es          : {suma}')
print(f'El Promedio es      : {prom}')
print(f'Mayores al promedio : {len(mp)} - {mp}')
print(f'El numero mayor es  : {max(nums)}')
print(f'El numero menor es  : {min(nums)}')