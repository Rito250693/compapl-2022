#calculo de paga total de un trabajador 

print('calculando la paga de un trabajador \n\n')
nombre = input('dame el nombre ?')
horas = int(input('dame las horas trabajadas'))
paga = float(input('dame paga por hora'))
tasa = 0.3


#calculo
if horas <=40:
    pagabruta = horas * paga
else:
    extra = horas - 40
    pagabruta = (40 * paga) + (extra * paga *2)    





impuesto = pagabruta * tasa
paganeta =pagabruta - impuesto

#salida
print('\n\nresumen de pagos \n\n')
print(f'el trabajador {nombre}, trabajo {horas}, con una paga de {paga} por hora')
print(f'la paga bruta es ={pagabruta}')
print(f'impuesto ={impuesto}')
print(f'paga neta = {paganeta}')
