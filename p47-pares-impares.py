#imprimir pares o impares de uno o dos hasta n y su suma

import os



while(True):
    os.system('cls')

    n=int(input('hasta donde quieres llegar ? '))


    #pares
    s=0
    print('numeros pares\n')
    for x in range(2,n+1,2):
        print(x,end=' ')
        s = s + x
    print(f'\n Suma {s}')
    #impares
    s=0
    print('\n numeros inpares\n')
    for x in range(1,n+1,2):
        print(x,end=' ')
        s = s + x
    print(f'\n Suma {s}')
    
    res = input('\n Deseas continuar (S/N) ').upper()
    if res == 'N':
        break
print('gracias por usar el sistema')