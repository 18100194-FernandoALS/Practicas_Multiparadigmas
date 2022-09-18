#2 Manejo y manipulación de elementos de una lista
# Escribir un programa que almacene el abecedario en una lista,
# elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.

from itertools import count
import string
abcdario = list(string.ascii_lowercase)

i = len(abcdario) - 1

for letra in range(i,1,-1):
    if letra % 3 == 0 and letra != 1:
        #del abcdario[(letra)]
        abcdario.pop(letra)
        i = i - 1
print(abcdario)
