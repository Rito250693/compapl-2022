#imprime la tabla de multiplicar deseada del 1 al 10
import os


c=1
while(True):
    os.system('cls')#este comando elimina la pantalla antes de iniciar el prigrama y poder ver todo de una manera mas limpia es de suma inportancia >>>>>>>>>
    print('imprime la tabla de multiplicar deseada del 1 hasta N')
    t=int(input('\n que tabla quieres ? '))
    n=int(input('hasta que numero quieres la tabla ? '))

    c=1
    while(c<=n):
     print(f'{c} x {t} = {c*t}')
     c+=1
    res=input('\nDeseas continuar (S/N) ? ').upper()
    if res=='N':
        break
print('\n gracias por utilizar este programa')