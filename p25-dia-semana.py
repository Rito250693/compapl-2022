#dado de un numero entero determinar que dia de la semana es ya que el 1 es correspondiente al dia domingo

print('dado un numero del 1-7 determinar que dia de la semana es \n')
print('dame un numero [1] [2] [3] [4] [4] [5] [6] [7]')
dia=int(input('elige una opcion  '))

if dia==1:
    print(f'el numero {dia} corresponde al dia Domingo' )
elif dia==2:
    print(f'el numero {dia} corresponde al dia lunes' )
elif dia==3:
    print(f'el numero {dia} corresponde al dia martes' )
elif dia==4:
    print(f'el numero {dia} corresponde al dia miercoles' )
elif dia==5:
    print(f'el numero {dia} corresponde al dia jueves' )
elif dia==6:
    print(f'el numero {dia} corresponde al dia viernes' )
elif dia==7:
    print(f'el numero {dia} corresponde al dia sabado' )
else:
    print('error de capa 8')