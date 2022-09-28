#el usuario ingresara la temperatura inicial y final en grados y la convertira a farenheit

import os

while(True):
    os.system("cls")
    ti=int(input('Dame la temperatura en centigrados'))
    tf=int(input('dame la temperatura final en centigrados'))

    c=ti
    while c<=tf:
        farenheit=(c*(9/5))+32
        print(f'{c}°C\t->\t{farenheit:.2f}°F')
        c+=1
    opc=input('Deseas Continuar (s/N): ').upper()
    if opc=='N':
        break
