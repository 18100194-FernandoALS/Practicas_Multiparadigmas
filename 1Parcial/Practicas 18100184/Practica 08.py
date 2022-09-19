#8 Resumen y multi-solución
# 8.1.-Definir una clase usuario que contenga como atributos:
# Usuario
# Contraseña
# Rol
# Nombre
# CURP
# Ciudad

class Usuario:
    @property 
    def usuario(self):
        return self._usuario
    @usuario.setter
    def usuario(self,a):
        self.usuario = a
    
    @property
    def password(self):
        return self._password
    @password.setter
    def password(self,a):
        self.password = a

    @property
    def rol(self):
        return self._rol
    @rol.setter
    def rol(self,a):
        self.rol = a

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self,a):
        self.nombre = a

    @property
    def CURP(self):
        return self._CURP
    @CURP.setter
    def CURP(self,a):
        self.CURP = a

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