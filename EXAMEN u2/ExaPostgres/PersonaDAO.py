from cursorPool import CursorDelPool
from persona import Persona
from Conexion import Conexion
from logger_base import log

class PersonaDAO:
    _SELECCIONAR = "SELECT * FROM persona ORDER BY id"
    _SELECCIONA = "SELECT * FROM persona WHERE correo = %s"
    _INSERT = "INSERT INTO persona(nombre,edad,correo) VALUES (%s,%s,%s)"
    _ACTUALIZAR ="UPDATE persona SET nombre=%s,edad=%s, correo=%s WHERE id=%s"
    _ELIMINAR = "DELETE FROM persona WHERE id = %s"
    
    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:            
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            personas = []
            for r in registros:
                persona = Persona(r[0],r[1],r[2],r[3])
                personas.append(persona)
            return personas
    
            
    @classmethod
    def insertar(cls,persona):
        with CursorDelPool() as cursor:
            valores = (persona.nombre, persona.edad, persona.correo)
            cursor.execute(cls._INSERT, valores)
            return cursor.rowcount
            
    @classmethod
    def actualizar(cls,persona):
        with CursorDelPool() as cursor:
            valores = (persona.nombre, persona.edad, persona.correo, persona.id)
            cursor.execute(cls._ACTUALIZAR, valores)
            return cursor.rowcount

    @classmethod
    def eliminar(cls,persona):
        with CursorDelPool() as cursor:
            valores = (persona.id, )
            cursor.execute(cls._ELIMINAR, valores)
            return cursor.rowcount

if __name__ == '__main__':
    """persona1 = Persona(nombre="P", apellido = "s", email = "@", edad = 39)
    personasAgregadas = PersonaDAO.insertar()
    log.debug(personasAgregadas)"""
    
    log.debug(f"Personas seleccionadas {PersonaDAO.seleccionar()}")
    
    """ #Insertar
    persona1 = Persona(nombre="Prank", edad = 10, correo ="Pjdez@hotmail.com")
    personasInsertadas = PersonaDAO.insertar(persona1)
    log.debug(f"Personas insertadas {personasInsertadas}") """
    
    #Actualizar
    persona1 = Persona(id=1, nombre = "Fernando",  edad = 22, correo="ferandoa_ls@hotmail.com")
    personaActualizadas = PersonaDAO.actualizar(persona1)
    log.debug(f"Personas actualizadas {personaActualizadas}")
    
    #Eliminar
    persona1 = Persona(id=2)
    personaEliminada = PersonaDAO.eliminar(persona1)
    log.debug(f"Personas Eliminada {personaEliminada}")