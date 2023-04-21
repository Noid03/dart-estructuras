#Crear un algoritmo donde se solicite dos matrices por consola. Tanto la cantidad de columnas
#como de filas, deben ser ingresadas por teclado. Los elementos de las matrices deben ser
#generados de forma aleatoria (0 al 5). Estas dos matrices se deben sumar. Luego se solicita
#una tercera matriz. Al igual que las dos anteriores, se ingresan columnas y filas por consola, y
#sus elementos son generados aleatoriamente (0 a 5). Esta última matriz se restará con la
#matriz resultante entre la operación de suma

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

def suma_matriz():
    suma_matrices = np.add(m1,m2)
    return suma_matrices
suma_matrices =suma_matriz()
print("La suma entre la primera y segunda matriz es:")
print(suma_matrices)

filas1 =int(input("Ingresar la cantidad de filas que tendrán las matrices:\n"))
columnas1 =int(input("Ingresar la cantidad de columnas que tendrán las matrices:\n"))

m3 = np.random.randint(0,5, size=(filas1, columnas1))
print("La tercera matriz es: ", m3)

def resta_matriz():
    resta_matrices = np.rest(suma_matrices,m3)
    return resta_matrices
print("la resta entre el resultante de la suma de matrices y la tercera matriz es: ")
print(resta_matrices)

for i in range(filas1):
    for j in range(columnas1):
        print (m3[filas1][columnas1])