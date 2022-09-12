#generar numeros de uno a 200 sumarlos hasta obteer 100
# print('generar n numeros para obtener una ganancia')
# ganar = int(input('cuanto quieres ganar'))
# c=0
# s = 0
# while s< ganar :
    
#     c +=1
#     s +=c


# print('suma= ',s)
# print(f'use {c} numeros')
print('generar n numeros para obtener una ganancia')
ganar = int(input('cuanto quiers ganar ?'))
c = 0
suma =0
while c<ganar:
    c+=1
    suma+=c
    print(c,end=" ")
    if suma >= ganar:
     print('\n')
     break

print('suma > ', suma)