#Se desea imprimir la secuencia de números mostrados el numero de renglones que el usuario desee

print('Se desea imprimir la secuencia de números mostrados el numero de renglones que el usuario desee')
r=int(input('Dame un numero?'))

for i in range(1, r+1):
    for l in range(1, i+1):
        print(l,end='')
    print()