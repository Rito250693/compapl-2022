#calcular ela suma y el promedio de 3 calificaciones



print('calcular la suma y el promedio de tres calificaciones\n')
#c1 = input('dame calificacion 1')
#c1 = input('dame calificacion 2')
#c2 = input('dame calificacion 3')
print('dame tres calificaciones separadas por un espacio')
c1, c2, c3 =input().split()
c1, c2, c3 =[int(c1),int(c2),int(c3)]
suma= c1 + c2 + c3
prom = suma/3
print(f'los numeros fueron {c1}, {c2}, {c3}')
print(f'la suma de los numeros es {suma}')
print(f'el promedio es de {prom}')

