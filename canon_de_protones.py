from arma import Arma
import random

class Canon(Arma):

    def __init__(self):
        pass

    @property
    def nombre(self):
        self._nombre = "Cañon de protones"
        return self._nombre
    
    @property
    def damage(self):
        self._damage = 2
        return self._damage
    
    @property
    def precision(self):
        booleano = random.choice([True, False])
        self._precision = booleano
        return self._precision