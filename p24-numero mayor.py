#dados tres numeros mayores verfificar cual es el mayor 

print('verificador de numero mayor')
print('dame tres numeros enteros separados por un enter')

n1, n2, n3 =int(input()), int(input()), int(input())

if n1 > n2 and n1 > n3:
    print(f'{n1} es el numero mayor')

elif n2 > n1 and n2 > n3:
    print(f'{n2} es el numero mayor')
elif n3>n1 and n3>n2:
    print(f'{n3} es el numero mayor')
elif n1==n2 and n2==n3:
    print('los tres numeros son iguales')
