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
        self._usuario= usuario
        self._password = contraseña
        self._rol = rol
        self._nombre = nombre
        self._CURP = curp
        self._ciudad = ciudad
    
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
import sys
lusuario = ["FernandoL","JesusV","EduardoZ","LCastillo"]
lpassword = ["123Fer", "123Jes", "123Edu","Cas123"]
lrol = ["cliente","cliente","cliente","Administrador"]
lnombre = ["Fernando","Jesus","Eduardo", "Luis Daniel"]
lCURP = ["FE1","JE2","ED3","LDC4"]

def agregarRegistro(u,p,r,n,c):
    lusuario.append(u)
    lpassword.append(p)
    lrol.append(r)
    lnombre.append(n)
    lCURP.append(c)

def imprimirRegistro(ind):
    print(f'Usuario'.center(20,'='))
    print(f"Usuario: {lusuario[ind]}\nRol: {lrol[ind]}\nNombre: {lnombre[ind]}\nCurp: {lCURP[ind]}")
    print(f''.center(20,'='))

def imprimirRegistros():
    print(f'Usuario'.center(20,'='))
    print(f"Usuarios: {lusuario}\nRoles: {lrol}\nNombres: {lnombre}\nCurps: {lCURP}")
    print(f''.center(20,'='))
    

def comprobarRegistro(us,pas,rl,nom,curp):
    for i in lusuario:
        if i != us:
            for j in lpassword:
                if j != pas:
                    for k in lCURP:
                        if k != curp:
                            agregarRegistro(us,pas,rl,nom,curp)
                            print("\nRegistrado")
                            imprimirRegistro(-1)
                            sys.exit()
                        else:
                            print("El usuario ya existe")
                            sys.exit()
    
def Registro():
    print("Ingrese los siguientes datos:")
    usuario = input("Ingrese su usuario: ")
    password = input("Ingrese su contraseña: ")
    rol = "cliente"
    nombre = input("Ingrese su nombre: ")
    CURP = input("Ingrese su CURP: ")
    comprobarRegistro(usuario,password,rol,nombre,CURP)
    

def InicioSesion():
    print("Ingrese sus credenciales: ")
    usuario = input("Ingrese su usuario: ")
    password = input("Ingrese su contraseña: ")
    comprobarInicio(usuario, password)
    """if(comprobarInicio()):
        pass
    else:
        pass"""
        

def comprobarInicio(us, pas):
    for index, i in enumerate(lusuario):
        if i == us:
            for j in lpassword:
                if j == pas:
                    if (lrol[index] == "Administrador"):
                        imprimirRegistros()
                    else:
                        imprimirRegistro(index)

bandera = True
while (bandera):
    opcion = input("Seleccione una opcion: \n1.- Registro\n2.- Inicio de sesión\n3.- Salida\n")
    if( opcion == "1"): 
        bandera = False
        Registro()
        sys.exit()        
    if (opcion == "2"): 
        bandera = False
        InicioSesion()
        sys.exit()
    if (opcion == "3"): 
        bandera = False
        print("Nos vemos usuario.")
        sys.exit()
    else:
        print("Ingrese una opcion valida")
        continue


# 8.3.- Declarar un usuario con rol “Administrador” el cual al momento de iniciar sesión despliegue la información de todos los usuarios registrados al momento.
