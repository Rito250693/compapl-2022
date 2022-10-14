#contar letras numeros y sibolos en una frase
import os;os.system('cls')

print('contar letras, numeros y simbolos')

#frase='450 aniversario de la toma de zacatecas -2022'
frase=input('dame la fase? ')
let= dig= sim = 0
let1= dig1=sim1=''#se le deja en comillas para poder almacenar las variables que corresponden

print(frase)
print(f'\n la frase tiene {len(frase)} caracteres')

for l in frase:
    if l.isalpha():
        let= let+1
        let1+=l
    elif l.isdigit():
        dig=dig+1
        dig1+=l
    else:
        sim+=1
        if l!=" ":
            sim1+=l



print(f'\nletras: {let} {let1} \ndigitos: {dig}  {dig1}\nsimbolos: {sim}  {sim1}')