#crear un arreglo y ordenarlo de forma descendente
#luego ordenar ese mismo arreglo de forma aleatoria

import random
numeros = [16, 4, 9, 1, 3, 20, 8]
numeros.sort(reverse=True)
print(numeros)

def mezclar_numeros(lnumeros):
    numeros = numeros[:]
    Numeros_aleatorio = len(numeros)
    for i in range(Numeros_aleatorio):
        indice_aleatorio = random.randint(0, Numeros_aleatorio - 1)
        temporal = lista[i]
        lista[i] = lista[indice_aleatorio]
        lista[Numeros_aleatorio] = temporal
    return numeros