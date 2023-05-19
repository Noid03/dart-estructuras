import numpy as np
import random

filas =int(input("Ingresar la cantidad de filas que tendran las matrices\n"))
columnas =int(input("Ingresar la cantidad de columnas que tendrán las matrices:\n"))

m1 = np.random.randint(0,5, size=(filas, columnas)) 
m2 = np.random.randint(0,5, size=(filas, columnas))
print("La primera matriz es: ", m1)
print("La segunda matriz es: ", m2)

for i in range(filas):
    for j in range(columnas):
        print (m1[filas][columnas])
for i in range(filas):
    for j in range(columnas):
        print (m2[filas][columnas])

def resta_matriz():
    resta_matrices = np.rest(m1,m2)
    return resta_matrices
resta_matrices =resta_matriz()
print("La resta entre la primera y segunda matriz es:")
print(resta_matriz)

filas1 =int(input("Ingresar la cantidad de filas que tendrán las matrices:\n"))
columnas1 =int(input("Ingresar la cantidad de columnas que tendrán las matrices:\n"))

m3 = np.random.randint(0,5, size=(filas1, columnas1))
print("La tercera matriz es: ", m3)

def multiplicacion_matriz():
    multiplicacion_matrices = np.multiply(resta_matriz, m3)
    return multiplicacion_matrices
multiplicacion_matrices= multiplicacion_matriz()
print("la multiplicacion entre la resta de las matrices y la tercera matriz es: ")
print(multiplicacion_matriz)

for i in range(filas1):
    for j in range(columnas1):
        print (m3[filas1][columnas1])
