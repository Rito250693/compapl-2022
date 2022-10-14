#dado un dia de la semana imprimir la paga correspondiente a ese dia de la semana 
import os;os.system('cls')
dias=['lunes','martes','miercoles','jueves','viernes','sabado','domingo']
paga=[100,200,300,400,500,600,700]
print('#dado un dia de la semana imprimir la paga correspondiente a ese dia de la semana ')

dia=input('dame un dia de la semana con letra\n')

if dia in dias:
    print('si esta')
    print(f'Elegiste el dia {dia}')
    pos= dias.index(dia)
    print(pos)
    print(f'le corresponde un pago de : {paga[pos]}')
else:
    print('no esta ')