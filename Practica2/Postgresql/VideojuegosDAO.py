from cursorPool import CursorDelPool
from TablasPostgres import Videojuego
from Conexion import Conexion
from logger_base import log

class VideojuegosDAO:
    _SELECCIONAR = "SELECT * FROM videojuego ORDER BY idjuego"
    _INSERT = "INSERT INTO videojuego(titulo,genero,lanzamiento) VALUES (%s,%s,%s)"
    _ACTUALIZAR = "UPDATE videojuego SET titulo=%s, genero=%s, lanzamiento=%s WHERE idjuego=%s"
    _ELIMINAR = "DELETE FROM videojuego WHERE idjuego=%s"
    
    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            juegos = []
            for r in registros:
                juego = Videojuego(r[0],r[1],r[2],r[3])
                juegos.append(juego)
            return juegos
        
    @classmethod
    def insertar(cls,juego):
        with CursorDelPool() as cursor:
            valores = (juego.titulo, juego.genero, juego.lanzamiento)
            cursor.execute(cls._INSERT, valores)
            return cursor.rowcount
        
    @classmethod
    def actualizar(cls,juego):
        with CursorDelPool() as cursor:
            valores = (juego.titulo, juego.genero, juego.lanzamiento, juego.idJuego)
            cursor.execute(cls._ACTUALIZAR, valores)
            return cursor.rowcount
        
    @classmethod
    def eliminar(cls,juego):
        with CursorDelPool() as cursor:
            valores = (juego.idJuego, )
            cursor.execute(cls._ELIMINAR, valores)
            return cursor.rowcount
        
if __name__ == '__main__':
    """ 
    #Leer
    log.debug(f'Videojuegos en la base de datos: {VideojuegosDAO.seleccionar()}')
     """
    #Insertar
    j1 = Videojuego(titulo = "Castlevania", genero="Plataforma", lanzamiento=1994)
    juegosIn = VideojuegosDAO.insertar(j1)
    log.debug(f'Videojuegos agregados a la base de datos {juegosIn}')
    
    """ #Actualizar
    j2 = Videojuego(idJuego=1, titulo="Castlevania", genero="Plataforma", lanzamiento=1994)
    juegosIn = VideojuegosDAO.actualizar(j2)
    log.debug(f'Videojuegos actualizados {juegosIn}')
    
    #Eliminar
    j3 = Videojuego(idJuego= 3)
    JuegosEl = VideojuegosDAO.eliminar(j3)
    log.debug(f'Juegos eliminados {JuegosEl}') """