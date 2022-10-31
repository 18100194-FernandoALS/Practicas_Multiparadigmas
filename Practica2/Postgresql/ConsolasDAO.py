from cursorPool import CursorDelPool
from TablasPostgres import Consola
from Conexion import Conexion
from logger_base import log

class ConsolasDAO:
    _SELECCIONAR = "SELECT * FROM consola ORDER BY idconsola"
    _INSERT = "INSERT INTO consola(consola, modelo, año) VALUES (%s,%s,%s)"
    _ACTUALIZAR = "UPDATE consola SET consola=%s, modelo=%s, año=%s WHERE idcompañia=%s"
    _ELIMINAR = "DELETE FROM consola WHERE idconsola=%s"
    
    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            consolas = []
            for r in registros:
                consola = Consola(r[0], r[1], r[2], r[3])
                consolas.append(consola)
            return consolas
        
    @classmethod
    def insertar(cls,con):
        with CursorDelPool() as cursor:
            valores = (con.consola, con.modelo, con.año)
            cursor.execute(cls._INSERT, valores)
            return cursor.rowcount
        
    @classmethod
    def actualizar(cls,con):
        with CursorDelPool() as cursor:
            valores = (con.consola, con.modelo, con.año, con.idconsola)
            cursor.execute(cls._ACTUALIZAR, valores)
            return cursor.rowcount
        
    @classmethod
    def eliminar(cls, con):
        with CursorDelPool() as cursor:
            valores = (con.idconsola, )
            cursor.execute(cls._ELIMINAR, valores)
            return cursor.rowcount
        
if __name__ == '__main__':
    
    #Leer
    log.debug(f'Consolas almacenadas: {ConsolasDAO.seleccionar()}') 
     
    #Insertar
    consola1 = Consola(consola="Xbox", modelo= "360", año=2006)
    consolaIn = ConsolasDAO.insertar(consola1)
    log.debug(f'Consolas agregadas: {consolaIn}')
     
    #Actualizar
    consola2 = Consola(consola="Playstation 2", modelo= "Fat", año=2006, idConsola=1)
    consolaUp = ConsolasDAO.insertar(consola2)
    log.debug(f'Consolas actualizadas: {consolaUp}')
    
    #Eliminar
    consola3 = Consola(idConsola=2)
    consolaDel = ConsolasDAO.insertar(consola3)
    log.debug(f'Consolas eliminadas: {consolaDel}') 