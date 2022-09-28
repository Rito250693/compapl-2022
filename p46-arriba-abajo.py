#imprimir de numeros de 1 a n y de n a 1 segun elija el usuario
import os



while(True):
    os.system('cls')

    print('imprimir de numeros de 1 a n y de n a 1 segun elija el usuario')
    print('[1] numeros de 1 hasta n ')
    print('[2] numeros de n a 1 ')


    op=int(input('\nelige una opcion?'))
    n=int(input('dame el limite de n? '))

    if op==1:
        print(f'imprimir numeros del 1 a {n} ')
        for x in range(1,n+1,1):
            print(x,end=' ')
    elif op==2:
        print(f'imprimir numeros de {n} a 1 ')
        for x in range(n,0,-1):
            print(x,end=' ')
    res = input('\n Deseas continuar (S/N) ').upper()
    if res == 'N':
        break
print('gracias por usar el sistema')