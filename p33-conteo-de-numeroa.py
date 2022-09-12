#cuenta numeros , los suma, suenta : positivos, negativos, para parar 999


numero=cuenta =suma=0
cuenta_positivos=cuenta_negativos=cuenta_ceros=0

print('cuenta numeros , los suma, suenta : positivos, negativos, para parar 999')


while(True):
    numero =int(input('numero ? '))
    if numero != 999:
        cuenta+=1
        suma+=numero
        if numero>0:
            cuenta_positivos+=1
        elif numero<0:
            cuenta_negativos+=1
        else:
            cuenta_ceros+=1
    else:
        break
print(f'se introdujeron {cuenta} numeros')
print('la suma de los numeros es', suma)
print('positivos :',cuenta_positivos)
print('negativos :',cuenta_negativos)
print('ceros     :', cuenta_ceros)