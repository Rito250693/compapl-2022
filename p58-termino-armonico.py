#Se desea imprimir la secuencia de términos armónicos el numero de renglones que el usuario desee y su suma

print('imprimir la secuencia de términos armónicos el numero de renglones que el usuario desee')

n= int(input('dame un numero'))
suma=0

for i in range(1,n+1):
    if i==1:
        print("1+",end=" ")
        suma+=1
    elif i==n:
        print(f"1/{i}",end=" ")
        suma+=(1/i)
    else:
        print(f'1/{i}',end='+')
        suma+=(1/i)
print(f'\nLa suma de los terminos armonicos es: {suma}')