#DAO
class Videojuego:
    def __init__(self, idJuego=None, titulo=None, genero=None, lanzamiento=None) -> None:
        self.IDj = idJuego
        self.titulo = titulo
        self.genero = genero
        self.lanzamiento = lanzamiento
    
    def __str__(self) -> str:
        return (f'{self.IDj} {self.titulo} {self.genero} {self.lanzamiento}')
    @property
    def idJuego(self):
        return self.IDj
    
    def titulo(self):
        return self.titulo
    
    def genero(self):
        return self.genero
    
    def lanzamiento(self):
        return self.lanzamiento
    
class Consola:
    def __init__(self, idConsola=None, consola=None, modelo=None, año=None) -> None:
        self.IDcl = idConsola
        self.consola = consola
        self.modelo = modelo
        self.año = año
        
    def __str__(self) -> str:
        return (f'{self.IDcl} {self.consola} {self.modelo} {self.año}')
    @property
    def idConsola(self):
        return self.IDcl
    
    def consola(self):
        return self.consola
    
    def modelo(self):
        return self.modelo
    
    def año(self):
        return self.año

class Compañia:
    def __init__(self, idCompañia=None, compañia=None, añoCreacion=None) -> None:
        self.IDcm = idCompañia
        self.compañia = compañia
        self.añoCreacion = añoCreacion
    
    def __str__(self) -> str:
        return (f'{self.IDcm} {self.compañia} {self.añoCreacion}')
    
    @property
    def idCompañia(self):
        return self.IDcm
    
    def compañia(self):
        return self.compañia
    
    def añoCreacion(self):
        return self.añoCreacion