from cursorPool import CursorDelPool
from contrato import Contrato
from Conexion import Conexion
from logger_base import log

class ContratoDAO:
    _SELECCIONAR = "SELECT * FROM contrato ORDER BY id"
    _INSERT = "INSERT INTO contrato(nocontrato, costo, fechainicio, fechafin) VALUES (%s,%s,%s,%s)"
    _ACTUALIZAR = "UPDATE contrato SET nocontrato = %s, costo=%s, fechainicio=%s, fechafin=%s WHERE id=%s"
    _ELIMINAR = "DELETE FROM contrato WHERE id=%s"
    
    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            contratos = []
            for r in registros:
                contrato = Contrato(r[0],r[1],r[2],r[3],r[4])
                contratos.append(contrato)
            return contratos
    
    @classmethod
    def insertar(cls,contrato):
        with CursorDelPool() as cursor:
            valores = (contrato.nocontrato, contrato.costo, contrato.fechainicio, contrato.fechafin)
            cursor.execute(cls._INSERT, valores)
            return cursor.rowcount
    
    @classmethod
    def actualizar(cls,contrato):
        with CursorDelPool() as cursor:
            valores = (contrato.nocontrato, contrato.costo, contrato.fechainicio, contrato.fechafin, contrato.id)
            cursor.execute(cls._ACTUALIZAR, valores)
            return cursor.rowcount
    
    @classmethod
    def eliminar(cls,contrato):
        with CursorDelPool() as cursor:
            valores = (contrato.id, )
            cursor.execute(cls._ELIMINAR, valores)
            return cursor.rowcount
        
if __name__ == '__main__':
    #READ
    """ log.debug(f'Contratos: {ContratoDAO.seleccionar()}') """
     
    #INSERT
    """ c1 = Contrato(nocontrato=2011041, costo=230, fechainicio='22/10/2020', fechafin="10/11/2020")
    contratoIn = ContratoDAO.insertar(c1)
    log.debug(f'Contratos agregados: {contratoIn}') """
    
    #UPDATE
    c2 = Contrato(id= 1, costo=230, fechainicio="22/10/2020", fechafin="10/11/2020")
    contratoUP = ContratoDAO.actualizar(c2)
    log.debug(f'Contratos actualizados: {contratoUP}')
   
    #DELETE
    c3 = Contrato(id=3)
    contradoDEL = ContratoDAO.eliminar(c3)
    log.debug(f'Contratos eliminados: {contradoDEL}')