# uso de finciones trigonometricas
import math

print('uso de las funciones trigonometricas en pyton')
angulo = int(input('Dame un angulo en radianes ?'))
seno = math.sin(angulo)
coseno = math.cos(angulo)
tangente =math.tan(angulo)
grados =math.degrees(angulo)

#print(f'seno {seno}, coseno {tangente}, grados {grados}')

salida =(
"resumen de funciones trigonometricas\n"
f"el seno es{seno:.2f}\n"
f"el coseno es {coseno:.2f}\n"
f"la tangete es {tangente:.2f}\n"
f"el angulo es {angulo:.2f} en radianes,\n equivalente a {grados:.2f} grados \n"

)
print(f'salida{salida}')