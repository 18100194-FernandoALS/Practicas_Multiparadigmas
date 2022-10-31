class Persona:
    def __init__(self, id=None, nombre=None, edad=None, correo=None)->None:
        self.ID = id
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
        
    def __str__ (self) -> str:
        return (f'{self.ID} {self.nombre} {self.edad} {self.correo}')
    @property
    def id(self):
        return self.ID
    
    def nombre(self):
        return self.nombre
    
    def edad(self):
        return self.edad
    
    def correo(self):
        return self.correo