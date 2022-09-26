#8 Resumen y multi-solución
# 8.1.-Definir una clase usuario que contenga como atributos:
# Usuario
# Contraseña
# Rol
# Nombre
# CURP
# Ciudad

#from tabulate import tabulate
#import pandas as pd
import os
class Usuario:
    def __init__(self, usuario, password,rol, nombre, curp, ciudad) -> None:
        self.usuario = usuario
        self.password = password
        self.rol = rol
        self.nombre = nombre
        self.curp = curp 
        self.ciudad = ciudad
    def __str__(self) -> str:
        return f'Usuario: {self.usuario}, {self.password}, {self.rol}, {self.nombre}, {self.curp}, {self.ciudad}'

"""
8.2.-Realizar un programa que contenga el siguiente menú
1.- Registro
2.- Inicio de sesión
3.- Salida
La opción de registro solicitara al usuario registrarse solicitando la información de los atributos la clase exceptuando el atributo Rol 
que por defecto será rol cliente, no se permitirán usuarios con CURP repetido en caso de mostrar mensaje de “El usuario ya existe”
La opción de inicio de sesión permitirá al usuario introducir sus credenciales al ser correctas desplegar en pantalla la información del usuario
 de lo contrario mostrar mensaje de “datos incorrectos“
"""

usuarios = {}
miUsuario = Usuario("Eduardo2022","1234","Administrador","Eduardo", "GOZE000712HTSMXDA1", "Nvo Laredo") #8.3
#usuarios.append(miUsuario)
usuarios["Eduardo2022"] = miUsuario
def Registro():
    print("Ingrese los siguientes datos:")
    usuario = input("\nIngrese su usuario: ")
    password = input("\nIngrese su contraseña: ")
    rol = "usuario"
    nombre = input("\nIngrese su nombre:")
    CURP = input("\nIngrese su CURP:")
    ciudad = input("\nIngrese la ciudad: ")
    insertar = True
    os.system ("cls")
    #for usuario in usuarios:
    for curp in usuarios:
        if CURP == curp:
            print("Este CURP ya se uso previamente con otro usuario")
            insertar = False

    if insertar:
        miUsuario = Usuario(usuario,password,rol,nombre,CURP,ciudad)
        usuarios[miUsuario.usuario] = miUsuario


def InicioSesion():
    os.system ("cls")
    print("Ingrese sus credenciales: ")
    username = input('Username: ')
    password = input('Password: ')


    if username in usuarios.keys():
        usuario = usuarios[username]
        if usuario.password == password:
            if usuario.rol == 'Administrador':
                os.system ("cls")
                print('---USUARIOS---')
                print ("{:<10} {:<20} {:<20} {:<15} {:<25}".format('Usuario','Nombre','CURP','Ciudad', 'Rol'))
                print("\n")
                for user in usuarios.values():
                    print ("{:<10} {:<20} {:<20} {:<15} {:<25}".format(user.usuario, user.nombre, user.curp, user.ciudad, user.rol), end='\n\n')
            else:
                os.system ("cls")
                print('--- USUARIO---')
                print(usuario)
                print("\n'")
        else:
            print("Contraseña incorrecta")
    else:
        print("El usuario no existe")

def lee_entero() -> int:
   while True:
       entrada = input("Seleccione una opcion: \n1.- Registro\n2.- Inicio de sesión\n3.- Salida\n")
       try:
           entrada = int(entrada)
           return entrada
       except ValueError:
           #print ("La entrada es incorrecta: escribe un numero entero")
           return 9

opcion = 0
while (opcion != 3):
    #opcion = int(input("Seleccione una opcion: \n1.- Registro\n2.- Inicio de sesión\n3.- Salida\n"))
    opcion = lee_entero()
    if( opcion == 1): 
        Registro()
        print("\n")
    if (opcion == 2): 
        InicioSesion()
        print("\n")
    if (opcion == 3): break
    else:
        #os.system ("cls")
        print("Ingrese una opcion valida\n")


# 8.3.- Declarar un usuario con rol “Administrador” el cual al momento de iniciar sesión despliegue la información de todos los usuarios registrados al momento.
