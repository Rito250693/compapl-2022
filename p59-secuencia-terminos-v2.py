#imprimir la secuencia de términos, el numero de renglones que el usuario desee y su suma

print('imprimir la secuencia de términos, el numero de renglones que el usuario desee y su suma')

n=int(input('Dame un Numero ?   '))

sum=""
suma=0.

for i in range(1,n+1):
    for x in range(1,i+1):
        print('1',end="")
        sum +="1"
    suma+=int(sum)
    sum=""
    if x!=n:
        print("+",end="")
print(f'\n La suma de terminos es : {suma}')