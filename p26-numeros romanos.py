#dado un numero entero mostrar su equivalente en numero romano 

print('dado un numero entero mostrar equivalente en numero romano')
print('dame un numero entero entre el 1 y 10')

n=int(input())

if n==1:
    print('en romano es l')
elif n==2:
    print('en romano es ll')
elif n==3:
    print('en romano es lll')
elif n==4:
    print('en romano es lV')
elif n==5:
    print('en romano es V')
elif n==6:
    print('en romano es Vl')
elif n==7:
    print('en romano es Vll')
elif n==8:
    print('en romano es Vlll')
elif n==9:
    print('en romano es Xl')
elif n==10:
    print('en romano es X')
else:
    print(f'Error {n} es un numero invalido')