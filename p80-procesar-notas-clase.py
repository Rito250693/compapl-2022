#procesar notas de clase hasta introducir 0


import os; os.system('cls')

print('procesar n calificaciones introducidas por el usuario')
print('introduce calificaciones de 0...10, usa 99 para parar\n')

n=0
nums=[]
suma=prom=0
#p=-0

while n!='0':
    n=int(input('Numero > '))
    if n>=0 and n<=100:
        nums.append(n)
        suma=suma+n
    else:
        print('X')

prom= suma / len(nums)

men=[]
mp=[]   
for num in nums:
    if num>prom:
        mp.append(num)
    elif num<prom:
        men.append(nums)


print(f'notas ingresadas      : {len(nums)} - {nums}')
print(f'La suma y promedio es : {suma,prom}')
#print(f'El Promedio es      : {prom}')
#print(f'Mayores al promedio : {len(mp)} - {mp}')
print(f'El numero menor es  : {min(nums)} - {men}')
print(f'El numero mayor es  : {max(nums)}')