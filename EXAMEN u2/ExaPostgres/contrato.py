class Contrato:
    def __init__(self, id=None, nocontrato=None, costo=None, fechainicio=None, fechafin=None)->None:
        self.ID = id
        self.nocontrato = nocontrato
        self.costo = costo
        self.fechainicio = fechainicio
        self.fechafin = fechafin
        
    def __str__(self) -> str:
        return (f'{self.ID} {self.nocontrato} {self.costo} {self.fechainicio} {self.fechafin}')
    @property
    def id(self):
        return self.ID
    
    def nocontrato(self):
        return self.nocontrato
    
    def costo(self):
        return self.costo
    
    def fechainicio(self):
        return self.fechainicio
    
    def fechafin(self):
        return self.FechaFin