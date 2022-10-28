#llenar un lista con los primeros n numeros impares

impares=[]

suma=0

promedio=0

n=int(input("Ingrese el valor de n: "))
for i in range(1,n+1,2):
    impares.append(i)
    suma+=i

print(f"Los numero impares son: {impares}")

promedio=suma/len(impares)

print(f"La suma es : {suma} y el promedio es: {promedio:.2f}")

divisibles=[]
sumaDivisibles=0
for i in impares:
    if i%3==0:
        divisibles.append(i)
        sumaDivisibles+=i
        
print(f"Los numeros divisibles entre 3 son : {divisibles} su suma es: {sumaDivisibles}")

busqueda=int(input("Ingrese un número a buscar: "))

if busqueda in impares:
    pos=impares.index(busqueda);
    print(f"Se encontro!!, en la posición : {pos}")
else:
    print("No se encontro");