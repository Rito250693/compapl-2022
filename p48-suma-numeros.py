#imprimir la suma y el promedio de n numeros introducidos por el usuario

print('imprimir la suma y el promedio de n numeros introducidos por el usuario\n')
c = int(input('cuantos numeros deseas ?'))

s=0

for x in range(1,c+1,1):
    n = int(input(f' numero {x} = '))
    s = s + n



print(f'la suma es {s}')
print(f'y el promedio es  {s/c}')