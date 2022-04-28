# superclase

class Arma():

    def __init__(self):
        self._damage = None
        self._precision = None
        self._nombre = None
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def damage(self):
        pass
    
    @property
    def precision(self):
        pass
