class Contrato_persona:
    def __init__(self, idpersona=None, idcontrato=None)-> None:
        self.idPersona =  idpersona
        self.idContrato = idcontrato
        
    def __str__(self) -> str:
        return (f'{self.idPersona} {self.idContrato}')
    @property
    def idpersona(self):
        return self.idPersona
    @property
    def idcontrato(self):
        return self.idContrato