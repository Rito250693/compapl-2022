#imprime la tabla de multiplicar que el usuario pide hasta donde la pida
import os

while(True):

    print('imprime la tabla de multiplicar que el usuario pide hasta donde lo desee')
    t=int(input('que tabla quieres?  '))
    n=int(input('hasta donde ?  '))

    for i in range(1,n+1):
        print(i,'x',t,'=',i*t)
    res = input('\n \n deseas continuar (S\N) ?').upper()
    if res=='N':
        break;