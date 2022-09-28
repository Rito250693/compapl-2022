#contar las bocales y consonantes en una frace

# frase ='''Al año los murcielagos hullen de la fuerte luz\
# que baja por el kiosco de wivex'''
frase=input('dame la frase')
voc=0
con=0
otr=0


print(frase,'\n')
print(f'la frase tiene{len(frase)} caracteres')

for letra in frase:
    if letra.isalpha():
        if letra in ('aeiou'):
            voc= voc+1
        elif letra in ('bcdfghjklmnñpqrstvxzwy'):
            con=con+1
    else:
        otr=otr+1

print('vocales = ',voc)
print('consonantes = ', con)
print('otros = ',otr)
