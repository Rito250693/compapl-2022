#se busca saber el volumen de un cilindro

print('se busca calcular el volumen de un cilidro con el radio  y altura')

radio = float(input('Dame el radio del cilindro  \n'))

altura = float(input('Dame la Altura del cilindro   \n'))

volumen = 3.1416 * (radio **2 )*altura

print(f'el volumen del cilindro es {volumen:.2f}')
