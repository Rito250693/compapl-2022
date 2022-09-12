#tabla de convercion de peso a dolar y a,libras
import os

while(True):
    os.system('cls')
    tc =19.91
    tcl =23.00

    print('tabla de convercion de peso a dolar')

    pi = float(input('Dame el valor en pesos: '))
    pf = float(input('valor de pesos final: '))

    c=pi
    print('\n Peso \t Dolar\t libra')
    print('-'*20)
    while(c<=pf):

     print(f'{c}\t{c / tc:.4f}\t{c/tcl:.4f}')
     c+=1

    print('-'*20)

    resp =input('Deseas continuar (S/N)').upper()
    if resp =='N':
        break