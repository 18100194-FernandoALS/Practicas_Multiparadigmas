#3 Entrada de datos y manipulación.
# Escribir un programa que permita al usuario capturar su nombre completo e imprima su nombre de manera inversa letra por letra

nombre = input("Ingrese su nombre: ")
nombreInverso = (nombre[::-1])
#nombreInverso = (''.join(reversed(nombre)))
for letra in nombreInverso:
    print(letra)