from arma import Arma

class Granada(Arma):

    def __init__(self):
        pass
    
    @property
    def nombre(self):
        self._nombre = "Granada antimateria"
        return self._nombre

    @property
    def damage(self):
        self._damage = 3
        return self._damage
    
    @property
    def precision(self):
        self._precision = False
        return self._precision