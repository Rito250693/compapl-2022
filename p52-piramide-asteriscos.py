#imprime un tringulo del caracter que el usuario desee

print('imprime un tringulo del caracter que el usuario desee')
r= int(input('de cuantos renglones lo quieres tu triangul ?'))
c= input('de que caracter deseas la piramide')

for i in range(1, r+1):
    for j in range(1,i+1):
        print(c ,end='')
    print()
