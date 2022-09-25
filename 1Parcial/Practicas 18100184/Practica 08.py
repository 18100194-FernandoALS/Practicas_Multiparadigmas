#8 Resumen y multi-solución
# 8.1.-Definir una clase usuario que contenga como atributos:
# Usuario
# Contraseña
# Rol
# Nombre
# CURP
# Ciudad

class Usuario:
    def __init__(self,usuario,contraseña,rol,nombre,curp,ciudad) -> None:
        self._user= usuario
        self._password = contraseña
        self._role = rol
        self._name = nombre
        self._curp = curp
        self._city = ciudad
    
    @property 
    def usuario(self):
        return self._usuario
    @usuario.setter
    def usuario(self,a):
        self._usuario = a
    
    @property
    def password(self):
        return self._password
    @password.setter
    def password(self,a):
        self._password = a

    @property
    def rol(self):
        return self._rol
    @rol.setter
    def rol(self,a):
        self._rol = a

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self,a):
        self._nombre = a

    @property
    def CURP(self):
        return self._CURP
    @CURP.setter
    def CURP(self,a):
        self._CURP = a
        
    @property
    def ciudad(self):
        return self._ciudad
    @ciudad.setter
    def ciudad(self,a):
        self._ciudad = a

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
def Registro():
    print("Ingrese los siguientes datos:")
    usuario = input("Ingrese su usuario: ")
    password = input("Ingrese su contraseña: ")
    rol = "usuario"
    nombre = input("Ingrese su nombre:")
    CURP = input("Ingrese su CURP:")

def InicioSesion():
    print("Ingrese sus credenciales: ")

opcion = input("Seleccione una opcion: \n1.- Registro\n2.- Inicio de sesión\n3.- Salida")

while (opcion != 0):
    if( opcion == 1): Registro()
    if (opcion == 2): InicioSesion()
    else:
        print("Ingrese una opcion valida")


# 8.3.- Declarar un usuario con rol “Administrador” el cual al momento de iniciar sesión despliegue la información de todos los usuarios registrados al momento.
