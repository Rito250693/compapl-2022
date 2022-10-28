#procesar un pedid de pizas

import os;os.system('cls')

ingr = {'T':1.5, 'P':3.5, 'C':3.74, 'A':0.40, 'E':4.0}
base=15
subtotal=0

pedido=input('Ingredientes [T]omate , [P]iña, [C]hampiñon, [A]guacate, [E]xtra queso?\n' ).upper()


for i in pedido:
    if i in 'TPCA':
        subtotal += ingr[i]

subtotal= subtotal+base

if subtotal >= 20:
    total = subtotal - (subtotal*0.05)
else:
    total= subtotal
print(f'subtotal sin descuento : {subtotal:.2f}')
print(f'el total con descuento : {total:.2f}')