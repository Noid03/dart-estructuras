#Crear un arreglo aleatorio de tamaño entre 10 a 30. Imprimir el arreglo
#creado y luego solicitar por consola la búsqueda de un elemento en
#específico del arreglo creado. Todo esto utilizando import array.

import array
import random
Numero =random.randint(10,30)
Arreglo = array.array('i', [random.randint(0, 100) for _ in range(Numero)])
print(Arreglo)

busqueda = int(input("Ingrese el elemento que desea buscar en el arreglo:\n"))
verificar = False
for elemento in Arreglo:
    if elemento == busqueda:
        verificar = True
        break
if verificar:
    print("El elemento",busqueda,"se encuentra en el arreglo")
else:
    print("El elemento",busqueda,"no se encuentra en el arreglo")
