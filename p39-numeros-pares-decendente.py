#imprimir los números pares desde 100 hasta el número que el usuario decida





while(True):
    print('numeros pares de 100 a n ')
    n=int(input('Hasta que numero deseas los pares?'))
    r = 100
    s = 0

    while r >= n :
        if n % 2 == 0 :
            print(r)
            s = s+n
        r= r-2
    print(f'el resultado de la suma es {s}')

