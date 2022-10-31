from cursorPool import CursorDelPool
from TablasPostgres import Compañia
from Conexion import Conexion
from logger_base import log

class CompañiasDAO:
    _SELECCIONAR = "SELECT * FROM compañia ORDER BY idcompañia"
    _INSERT = "INSERT INTO compañia(compañia, añocreacion) VALUES (%s,%s)"
    _ACTUALIZAR = "UPDATE compañia SET compañia=%s, añocreacion=%s WHERE idcompañia=%s"
    _ELIMINAR = "DELETE FROM compañia WHERE idcompañia=%s"
    
    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            compañias = []
            for r in registros:
                compañia = Compañia(r[0], r[1], r[2])
                compañias.append(compañia)
            return compañias
        
    @classmethod
    def insertar(cls,comp):
        with CursorDelPool() as cursor:
            valores = (comp.compañia, comp.añoCreacion)
            cursor.execute(cls._INSERT, valores)
            return cursor.rowcount
    
    @classmethod
    def actualizar(cls,compañia):
        with CursorDelPool() as cursor:
            valores = (compañia.compañia, compañia.añoCreacion, compañia.idCompañia)
            cursor.execute(cls._ACTUALIZAR, valores)
            return cursor.rowcount
        
    @classmethod
    def eliminar(cls, compañia):
        with CursorDelPool() as cursor:
            valores = (compañia.idCompañia, )
            cursor.execute(cls._ELIMINAR, valores)
            return cursor.rowcount
        
if __name__ == '__main__':
    
     #Leer
    c1 = CompañiasDAO.seleccionar()
    log.debug(f'Compañias en la base de datos: {c1}') 
    """
    #Insertar
    c2 = Compañia(compañia= "Sony", añoCreacion=1946)
    compañiaIn = CompañiasDAO.insertar(c2)
    log.debug(f'Compañias de videojuegos: {compañiaIn}')
    
    #Actualizar
    c3 = Compañia(compañia= "Atari", añoCreacion=1933, idCompañia= 2)
    compañiaUp = CompañiasDAO.actualizar(c3)
    log.debug(f'Compañias de videojuegos actualizadas: {compañiaUp}')
    
    """
    #Eliminar
    c4 = Compañia(compañia= "Sony", añoCreacion=1946, idCompañia= 3)
    compañiaDel = CompañiasDAO.eliminar(c4)
    log.debug(f'Compañias de videojuegos eliminadas: {compañiaDel}')