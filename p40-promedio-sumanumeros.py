#se desea calcular la suma y el promedio  de una serie de numeros introducidos

c=0
s=0
n=1

print('suma y promedio de n numeros (0 para cancelar) : ')
while n != 0:
    n=int(input('Dame el numero entero  '))
    if n!=0:
        s += n
        c += 1

if c == 0:
    print('no se recibieron datos ^w^')
else:
    prom = s / c
    print(f'fueron {c} numeros ingresados y la suma de los numeros es {s} el promedio es {prom}')
            
     
