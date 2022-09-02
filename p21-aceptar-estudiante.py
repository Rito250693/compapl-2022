#aceptar un estudiante de acuerdo a ciertos criterios4
print('aceptar un estudante de acuerdo a ciertos criterios')

nombre=input('dame tu nombre ')
edad =int(input('dame tu edad '))

if edad>=18:
    print('dame dos calificaciones: ')
    c1, c2 = int(input()), int(input())
    if c1>=8 and c2>=8:
        print(f'Bienbenido {nombre} a la universidad pato, tienes {edad} y tus calificaciones son {c1} y {c2}')
    else:
        print(f'no aceptamos calificaciones menores a 8 lo sentimos mucho {nombre}')
else:
    print(f'no aseptamos menores de edad, lo sentimos {nombre}')

