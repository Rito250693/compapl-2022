#calcula o imprime el factorial de un numero

print('imprime el factorial de un numero')

n = int(input('dame un numero entero'))
f=1
for i in range(1,n+1 ):
    print(i, end=' x' )
    f= f*i
print(f'el factorial es {f} ')