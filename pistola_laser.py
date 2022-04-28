from arma import Arma


class Pistola(Arma):

    def __init__(self):
        pass

    @property
    def nombre(self):
        self._nombre = "Pistola laser"
        return self._nombre

    @property
    def damage(self):
        self._damage = 1
        return self._damage
    
    @property
    def precision(self):
        self._precision = True
        return self._precision