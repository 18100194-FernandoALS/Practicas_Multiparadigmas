# 4 Entrada de datos y estructuración.
# Revisar su retícula para escribir un programa que cree un diccionario vacío para que el usuario capture las materias y créditos de su semestre preferido 
# (inferior a 8vo) al final imprimir en el formato “{asignatura}” tiene “{créditos}” créditos. 
# Y la suma de todos los créditos del semestre

reticula = {}
opcion = 1

def agregarMateria():
    nombreMateria = input('Ingrese el nombre de la materia: ')
    cantidadCreditos = int(input('Ingrese la cantidad de créditos: '))
    reticula[nombreMateria] = cantidadCreditos

while (opcion != 0):
    opcion = int(input('\n[0] Salir\n[1] Ingresar Materia\n'))
    if(opcion == 1): agregarMateria()

totalCreditos = 0
print('\nResumen:\n----------')
for asignatura, creditos in reticula.items():
    print(f'{asignatura} tiene {creditos} créditos.')
    totalCreditos += creditos

print(f'\nTotal de créditos: {totalCreditos}')