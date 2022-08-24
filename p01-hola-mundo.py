# leer datos y envia saludo

print('leyendo datos')
nombre =input('Dame tu nombre ?')# leer una cadena de caracteres
edad = int(input('Dame tu edad ?'))# leer una cadena luego la ombierto a un numero entero
peso =float(input('Dame tu peso?'))# leer una cadena luego la combierto a flotante o numeros con decimales 

print(f'hola{nombre} Bienvenido a Pyton, tu rdad es{edad}, tu peso es{peso}')

print(type(nombre))
print(type(edad))
print(type(peso))
