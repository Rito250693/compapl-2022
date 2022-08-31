#calcul de hipotenuza de un triangulo
import math #importe la libreria de matematicas ya que se utilisara la raiz cuadrada para este ejercicio

print('se desea saber cual es la hipotenuza de un triangulo')

loglado1 = int(input("ingrese el valor  del primer lado o cateto ")) #este recibe el primer lado

loglado2 = int(input('ingresa el valor del segundo lado o cateto ')) #este recibe el segundo lado

hipotenusa = math.sqrt(loglado1 ** 2 + loglado2 **2)# los lados los eleve a la segunda potencia ya que crei
#conveniente el simplificarlo

print(f'la hipotenusa es {hipotenusa:.2f}')