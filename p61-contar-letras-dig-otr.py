#contar letras, numeros y simbolos




print('contar letras, numeros y simbolos')

#frase='450 aniversario de la toma de zacatecas -2022'
frase=input('dame la fase? ')
let= dig= sim = 0

print(frase)
print(f'\n la frase tiene {len(frase)} caracteres')

for l in frase:
    if l.isalpha():
        let= let+1
    elif l.isdigit():
        dig=dig+1
    else: sim=sim+1
print(f'\nletras: {let}\ndigitos: {dig}\nsimbolos: {sim}')