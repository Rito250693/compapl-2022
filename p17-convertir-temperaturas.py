#convertir temperaturas celsius a farebheit  y viseversa

print('convertir temperaturas celsius a farebheit  y viseversa')
print('[C] convertir a farenheit')
print('[F] convertir a farenheit')
opcion = str.upper(input('Elige?'))#la funcion str es para poder convertir en mayusculas las letras ingresadas y no se tenga problema alguno

if opcion=='C':
    print('\n elegiste convertir a grados centigrados')
    temp =float(input('dame los grados celcius '))
    res = (temp -32 )*5 / 9
    print(f'{temp} grados celsius equivale a {res:.2f}°F')
else:
    print('\n elegiste convertir a grados centigrados ')
    temp =float(input('dame los grados farenheit'))
    res = (temp *9/5) + 32
    print(f'{temp} grados farenheit equivale a {res:.2f}°C')