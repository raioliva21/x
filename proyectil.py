from xmlrpc.client import boolean
from arma import Arma


class Proyectil():

    def __init__(self) -> None:
        self._damage = None
        self._impact = None
        self._destination = None
    
    @property
    def damage(self):
        return self._damage
    
    @damage.setter
    def damage(self, damage):
        if isinstance(damage, int):
            self._damage = damage
        else:
            return False
    
    @property
    def destination(self):
        return self._destination
    
    @destination.setter
    def destination(self, destination):
        if isinstance(destination, list):
            self._destination = destination
        else:
            return False

    @property
    def impact(self):
        return self._impact
    
    @impact.setter
    def impact(self, impact):
        if isinstance(impact, bool):
            self._impact = impact
        else:
            return False