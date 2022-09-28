#dividir una frase  en palabras y contar consonantes y vocales




print('dividir una frase  en palabras y contar consonantes y vocales')

frase ='''Al año los murcielagos hullen de la fuerte luz\
que baja por el kiosco de wivex'''

print(f'{len(frase)} - {frase} \n')

palabras= frase.split() #dividir en palabras 

print(f' lista de palabras: {palabras,} ,\n')

print(f"{'Divicion de palabras':-^35}")
for palabras in palabras:
    print(f'{len(palabras):>4} - {palabras:<12}', end='')
    v=c=0
    for letra in palabras:
        print (letra)
        if letra.isalpha():
            if letra.lower() in 'aeiou': v=v+1
            else: c =c+1
    print(f'-v:{v} c:{c} ')

print(f"{'fin':-^35}")