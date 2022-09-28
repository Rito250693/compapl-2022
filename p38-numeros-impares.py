#Se desea imprimir los números impares de forma ascendente desde 1 hasta el número que el usuario decida



n=0
while(True):
    print('imprimir los números impares de forma ascendente desde 1 hasta el número que el usuario decida')
    x=int(input('hasta que numero deseas llegar? '))

    while n<x:
        n= n+1
        if n%2:
            print(n)
        

    res=input('\nDeseas continuar (S/N) ? ').upper()
    if res=='N':
        break
print('\n gracias por utilizar este programa')