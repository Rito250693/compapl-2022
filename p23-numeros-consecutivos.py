#dados tres numeros enteros, verificar sis son consecutivos




print('verificara si son consecutivos o no ')
print('dame tres numeros enteros separados por un enter')

n1, n2, n3 =int(input()),int(input()), int(input())


if n1==n2+1 and n2==n3+1 or n1==n2-1 and n2==n3-1:
    print(f'{n1} {n2} y {n3} son consecutivos')
else:
    print(f'{n1} {n2} y {n3} no son consecutivos')