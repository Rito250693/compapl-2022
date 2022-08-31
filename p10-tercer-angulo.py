# en este ejercicio se busca el tercer angulo de un triangulo

lado1 = int(input('Ingresa el primer lado '))
lado2 = int(input('Ingresa el segundo lado'))

lado3 = 180 - (lado1 + lado2)

print(f'el tercer angulo mide {lado3}cm')