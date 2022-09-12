#clculo de promedio
print(' calculo de promedio de calificaciones')
print('dame 5 calificaciones separadas con un enter')

c1,c2,c3,c4,c5 = float(input()),float(input()),float(input()),float(input()),float(input())

res=c1+c2+c3+c4+c5
prom=res/5

if prom<=6:
    print(f'tu promedio es de {prom} Estas reprobado')
elif prom>6.1 and prom<=7:
    print(f'tu promedio es de {prom} pasaste de pansaso')
elif prom>7.1 and prom<=8:
    print(f'tu promedio es de {prom} Muy bien Puedes Mejorar')
elif prom>8.1 and prom<=9:
    print(f'tu promedio es de {prom} Excelente sigue asi')
elif prom>9.1 and prom<=10:
    print(f'tu promedio es de {prom} perfecto tu esfuerzo valio mucho la pena')
print('gracias por usar el programa ')