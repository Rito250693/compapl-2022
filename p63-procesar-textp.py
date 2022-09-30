#procesar un texto usando funciones
import os
# txt='''programar en python es una tarea\
# que requiere tiempo y constancia, la practica es lo que\
# da la experiencia'''
txt=input('dame la frase')

os.system('cls')
print(f'Texto: {len(txt)} - {txt}')

pal = input('Dame la palabra')
pos = txt.find(pal)

if pos!=-1:
    #print(f'la palabra {pal} fue encontrada')
    if txt.startswith(pal):
        print(f'la palabra {pal} esta al inicio del texto')
    elif txt.endswith(pal):
        print(f'la palabra {pal} esta al final del texto')
    else:
        print(f'la palabra {pal} aparece en la posicion {pos}')
        print(f'la palabra {pal} aparece {txt.count(pal)} veces')
        txt2=txt.replace(pal, pal .upper())
        print(f'texto modificado :{txt2} ')
else:
    print(f'la palabra {pal} no fue encontrada')

print('\n Procesamiento de texto\n')
print(f'Mayusculas : {txt.upper()}')
print(f'Munusculas : {txt.lower()}')
print(f'Titulo     : {txt.title()}')

txt3 = txt.split()
print(f'\Separar  : {txt3}')
print(f'\n Unir   : {",".join(txt3)} ')
