from cursorPool import CursorDelPool
from contrato_persona import Contrato_persona
from Conexion import Conexion
from logger_base import log

class Contrato_PersonaDAO:
    _SELECCIONAR = "SELECT * FROM contrato_persona"
    _INSERT = "INSERT INTO contrato_persona(idpersona, idcontrato) VALUES (%s,%s)"
    
    
    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            contratos = []
            for r in registros:
                contrato = Contrato_persona(r[0],r[1])
                contratos.append(contrato)
            return contratos
    
    @classmethod
    def insertar(cls,contrato):
        with CursorDelPool() as cursor:
            valores = (contrato.idpersona, contrato.idcontrato)
            cursor.execute(cls._INSERT, valores)
            return cursor.rowcount
        
if __name__ == '__main__':
    #READ
    log.debug(f'Contratos: {Contrato_PersonaDAO.seleccionar()}')
     
    #INSERT
    c1 = Contrato_persona(idpersona=2, idcontrato=1)
    contratoIn = Contrato_PersonaDAO.insertar(c1)
    log.debug(f'Contratos agregados: {contratoIn}')