#calcula el numero mayor al precionar 0 finaliza el proceso

print('calcula el numero mayor (precona 0 para finalizar)')

m=0

while(True):
    num=int(input('Dame un nuero ?'))
    if num!=0:
        if num>m:
            m=num
    else:
        break
print(f'el numero mayor es {m}')