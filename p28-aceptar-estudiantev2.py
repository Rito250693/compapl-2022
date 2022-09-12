#aceptar estudiante si cumple con las normas 

print('aseptar estudiante con ciertos criterios')
nom=input('dame tu nombre \n')
ed=int(input('dame tu edad\n'))

if ed>21:
    print('Que sexo eres [F] femenino [M] Masculino')
    sx = str.upper(input('eige una opcion  '))
    if sx =='F':
        print('Dame 3 calificaciones separadas con un enter\n')
        c1,c2,c3=float(input()),float(input()),float(input()),  
        prom=c1+c2+c3
        cl=prom/3
        if cl>8 and cl <=10:
            print(f'bienvenida {nom} a la universidad Kity Kat SA ')
            print(f'tu promedio es de {cl:.1f} y eres buena candidata para la institución')
        else:
            print(f'lo sentimos tu promedio es de {cl:.1f} y no alcansa para que ingresesa la institucion')
    else:
        print('lo sentimos esta escuela es solo para mujeres')

else:
    print('lo sentimos solo admitimos mayores de 21 años')