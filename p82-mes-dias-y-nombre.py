#dado un numero determinar el mes y cuantos dias tiene 

import os;os.system('cls')
nmes=['','1','2','3','4','5','6','7','8','9','10','11','12',]
mes=['','Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciemre']
dias=[0,31,28,31,30,31,30,31,31,30,31,30,31]
print('dado un dia de la semana imprimir la paga correspondiente a ese dia de la semana ')

num=input('dame un numero de un mes\n')

if num in nmes:
    print(f'Elegiste el numero {num}')
    pos=nmes.index(num)
    print(f'{mes[pos]} , {dias[pos]}')