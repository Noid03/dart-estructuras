#Crear un algoritmo que permita guardar los nombres y el RUT de 5
#personas sin perder ninguna de ellas. El usuario tiene que ingresar la
#información de cada persona por consola.
#Se debe imprimir los arrays de nombres y RUT para luego ordenarlas
#alfabéticamente y ascendentemente respectivamente

Nombre:input("cual es su nombre?")
Rut:input("cual es su rut?")
for subject in Nombre:
    Nombre= input("¿Cual es su nombre"+ subject+ "?")
for subject in Rut:
    Rut= input("¿Cual es su rut"+ subject+ "?")
for i in range(len(Rut)):
    print(Nombre[i] + " tu rut es " + Rut[i])