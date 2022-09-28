#imprime las tablas de multiplicar que el usuario pida y asta donde la pida
print('imprime las tablas de multiplicar hasta el numero que desees')
t=int(input('hasta que tabla quieres? '))
m= int(input('hasta donde la quieres ? '))

for i in range(1, t+1):
    print('tabla del',i)
    for j in range(1,m+1):
        print(f'{i} x {j} = {i*j}')
    print(' ')
