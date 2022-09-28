#imprimir los numeros de 100 a uno con ciclo for

# for x in range(100,0,-1):
#     print(x,end=' ')


# print('ímprimir los numeros de 100 a n usando for')

# n=int(input('hasta donde?'))

# for x in range(100,n-1,-1):
#     print(x,end=' ')



print('ímprimir los numeros de 100 a n en decrementos de m usando for')

n=int(input('hasta donde? '))
m=int(input('decremento? '))

for x in range(100,n-1,-m):
    print(x,end=' ')