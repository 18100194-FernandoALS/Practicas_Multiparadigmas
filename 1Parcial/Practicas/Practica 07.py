#7 Formateo y conversiones
#
# Escribir un programa que muestre un menú con 2 opciones la primera opción 
# “1.- Imprimir YYYY/MM/DD” 
# “2.- Imprimir MM/DD/YYYY” 
# una vez seleccionada la opción imprimir la fecha del día de hoy en el formato seleccionado.

from datetime import date
opcion = int(input('1.- Imprimir YYYY/MM/DD\n2.- Imprimir MM/DD/YYYY\n'))
print(date.today().strftime("%Y/%m/%d" if opcion == 1 else "%m/%d/%Y"))