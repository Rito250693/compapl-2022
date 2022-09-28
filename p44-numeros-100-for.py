#imprimir los numeros del 1 al 100 usando ciclo for
#print('imprimir los numeros del 1 al 100 usando ciclo for')
#for x in range(1,101,1):
 #   print(x,end=' ')

# print('imprimir los numeros del 1 al 100 usando ciclo for')
# n =int(input('hasta donde quieres llegar'))

# for x in range(1,n+1,1):
#     print(x,end=' ')

print('imprimir los numeros del 1 al n en incrementos de m usando ciclo for')
n =int(input('hasta donde quieres llegar'))
m=int(input('incremento'))

for x in range(1,n+1,m):
    print(x,end=' ')