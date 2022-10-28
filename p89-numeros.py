#Crear tres conjuntos, uno por cada lista de números y mostrarlos ( A, B, C)

A={50,60,70,80,90,100,200}
B={60,90,100,300,400,500}
C={10,20,60,90,70,100,600,700}

print(f"Conjunto A: {A}")
print(f"Conjunto B: {B}")
print(f"Conjunto C: {C}")

print(f"Union A Y B: {A|B}")
print(f"Union B Y C: {B|C}")
print(f"Diferencia A Y C: {A-C}")
print(f"Diferencia simetrica B Y C: {B^C}")
print(f"Intersección B Y C: {B&C}")

if A.issubset(B):
    print(f"A {A} es subconjunto de B {B}")
else:
    print(f"A {A} no es subconjunto de B {B}")

if C.issubset(A):
    print(f"C {C} es subconjunto de B {A}")
else:
    print(f"C {C} no es subconjunto de B {A}")

if 100 in A:
    print("100 esta en A")
else:
    print("100 no esta en A")

if (60 in A) and (60 in B) and (60 in C):
    print("60 esta en A, B Y C")
else:
    print("60 no esta en A,B Y C")

if not 900 in C:
    print("900 no esta en C")
else:
    print("900 esta en C")