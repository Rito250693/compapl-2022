#dividir una frase  en palabra y contar consonantes y vocales
import os;os.system('cls')



print('dividir una frase  en palabra y contar consonantes y vocales')

#frase ='''Al año los murcielagos hullen de la fuerte luz\
#que baja por el kiosco de wivex'''

frase=input('Dame La frase?')

print(f'{len(frase)} - {frase} \n')

palabra= frase.split() #dividir en palabra 

print(f' lista de palabra: {palabra,} ,\n')

print(f"{'Divicion de palabra':-^35}")

for palabra in palabra:
    print(f'{len(palabra):>4} - {palabra:<12}', end='')
    v=c=0
    for letra in palabra:
        print (letra)
        if letra.isalpha():
            if letra.lower() in 'aeiou': v=v+1
            else: c =c+1
    print(f'-v:{v} c:{c} ')

print(f"{'fin':-^35}")