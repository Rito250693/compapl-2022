#imprimir un cuadro de caracteres


print('imprime un cuadrado del caracter que el usuario desee')
r = int(input('de cuantos renglones lo quieres tu cuadrado ?'))
s = int(input('cuantas columnas?'))
c = input('de que caracter deseas la piramide')

for i in range(1,r+1):
    for j in range(1,s+1):
        print(c,end='')
    print()