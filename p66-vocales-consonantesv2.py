#contar cuantas vocales y consonantes tiene una frase, imprima cuales son estas.

import os ; os.system('cls')

frase='El dia se pasa muy rapido'
voc=0
vocales=''# se declara una variable para que almacene las vocales y se hace con comillas vacias
con=0
consonantes=''# se declara la variable con comillas vacias para guardar las consonantes
otr=0

print(frase,'\n')
print(f'la frase tiene{len(frase)} caracteres')

for letra in frase:
    if letra.isalpha():
        if letra in ('aeiouAEIOU'):
            voc= voc+1#aqui se va incrementando la variable Voc
            vocales+=letra#aqui se van almacenando las letras que coinciden con lo solicitado(aeiou)
        elif letra in ('bcdfghjklmnñpqrstvxzwy'):
            con=con+1
            consonantes+=letra
    else:
        otr=otr+1


print('vocales = ',voc,vocales)#aqui se imprime el numero de bocales encontradas y se imprimen las vocales encontradas
print('consonantes = ', con,consonantes)
print('otros = ',otr)
