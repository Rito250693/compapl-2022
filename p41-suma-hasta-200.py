#calcular la suma de números introducidos por el usuario hasta que la suma sea >= 200
while(True):
    n=0
    s=0
    c=1
    print('calculo de numeros hasta que la suma sea <= que 200')

    while s < 200:
        n=int(input('dame un numero'))
        c+=1
        s+=n
    print(f'se ingresaron{c} numeros y la suma es {s}')
    opc=input('Deseas COntinuar(S/N):').upper();
    if opc=='N':
        break
