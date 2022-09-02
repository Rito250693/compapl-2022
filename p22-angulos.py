#mostrar el tipo de angulo en bace a los grados 
#<90 agudo  =90 y <180
print('mostrar el tipo de angulo en bace a los grados ')
angulo = int(input('dame un angulo entre 0 y 360°'))

if angulo>=0 and angulo<=360:
    
    if angulo<90:
        print('agudo')
    elif angulo ==90:
        print('Recto')
    elif angulo>90 and angulo<180:
        print('obtuso')
    elif angulo == 180:
        print('Llano')
    elif angulo > 180 and angulo<360:
        print('Concavo')

else:
    print(f'el angulo{angulo} esta fuera de rango')
