#formateo de datos , la nueva forma
import os; os.system('cls')

noms = 'Juan Carlos Pedro Luis Jose Maria Julian Teresa Francisco Leticia Rafael'
nombres=noms.split()
edad=25
sueldo=15345.1234
tasa=0.4

print('\n salida de datos con formato "f" ')
print(f'Nombre: { nombres[5]}, Edad: {edad}, sueldo: {sueldo:,.2f} Tasa: {tasa:.2%}')

print(f'\nNombres :{noms}')
print(f'\n Nombres: {nombres}')

print(f'{"Tabla de Datos":-^47}')
print(f"{'no':<6}{'Nombre':<15}{'Edad':^10}{'sueldo':>15}")
print('-'*47)

for i in range(len(nombres)):
    print(f'{i:<4}{nombres[i]:<15}{edad+i:^10}{edad*i*5:>15,.2f}')

print(f"{'Final':-^47}")