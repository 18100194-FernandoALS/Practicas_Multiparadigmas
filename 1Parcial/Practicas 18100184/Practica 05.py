#5 Manejo de información
#Escribir una función que reciba n parámetros de llave valor e imprima la información en formato “{llave}”: “{Valor}”

def ImprimeDiccionario(d): 
      
    for key in d: 
        print("key:", key, "Value:", d[key]) 
           
#ImprimeDiccionario({'a':1, 'b':2, 'c':3} )