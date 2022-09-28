#Se desea imprimir los pares de 2 a n y su suma
print('Se desea imprimir los pares de 2 a n y su suma')
n=int(input('dame un numero entero'))
suma=0
for i in range(2,n):
    print(i)
    suma+=i
print(f'la suma es {suma} ')