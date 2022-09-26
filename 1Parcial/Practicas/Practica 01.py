# #1 Funciones con n parámetros
# Escribir un programa que contenga una función que reciba n parámetros de tipo numérico y calcule el producto total.

def calcularProducto(*numeros):
    total = 1
    for num in numeros:
        total *= num
    print (total)

#calcularProducto(10,1,10.0)