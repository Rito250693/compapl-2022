#verificar si la suma de dos numeros es ugual aun tercero
print('verificar si la suma de dos numeros es ugual aun tercero')
print('dame3 numeros enteros separados por un espacio n')
n1, n2, n3 =  input().split()
n1, n2, n3 =[int(n1), int(n2), int(n3)]

if n1 + n2 + n3 == n3:
    print(f'{n1} + {n2} = {n3}')
elif n1+n3==n2:
     print(f'{n1} + {n3} = {n2}')
elif n2+n3==n1:
     print(f'{n2} + {n3} = {n1}')
elif n1==n2==n3:
    print('son iguales')
else:
    print('ninguna combinacion es igual')