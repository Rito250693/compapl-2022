#El usuario introduce un rango de números, luego se le muestra una tabla de conversiones
import os ; os.system('cls')

print('El usuario introduce un rango de números, luego se le muestra una tabla de conversiones')

inicio=int(input('Dame El rango inicial :'))
final=int(input('dame el rango final   :'))




print(f"{'Tabla de conversiones':^40}")
print(f'{" ":-^45}')
print(f'....Decimal____Exa____Octal_______Binario.....')
print(f'{" ":-^45}')
for i in range(inicio,final+1):
    print(f"|{i:>10}|{i:^10}|{i:<10o}|{i:>10b}|")

print(f'{" ":-^45}')
