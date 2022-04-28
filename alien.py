
from arma import Arma
from proyectil import Proyectil

"""<x coordinate> y <y coordinate>"""
class Alien():

    def __init__(self, x_coordinate, y_coordinate):
        self._x_coordinate = x_coordinate
        self._y_coordinate = y_coordinate
        self._health = 3
        self._hited = False
        self._arma = None
        self._num_ID = None
    
    @property
    def health(self):
        return self._health
    
    @property
    def hited(self):
        return self._hited
    
    @property
    def x_coordinate(self):
        return self._x_coordinate

    @x_coordinate.setter
    def x_coordinate(self, coordenada_x):
        if isinstance (coordenada_x, int):
            if 0 <= coordenada_x <= 15:
                self._x_coordinate = coordenada_x
            else:
                print("Coordenada 'x' ingresada supera limite.")
        else:
            return False
    
    @property
    def y_coordinate(self):
        return self._y_coordinate
    
    @y_coordinate.setter
    def y_coordinate(self, coordenada_y):
        if isinstance (coordenada_y, int):
            if 0 <= coordenada_y <= 15:
                self._y_coordinate = coordenada_y
            else:
                print("Coordenada 'y' ingresada supera limite.")
        else:
            return False
    
    def hit(self):
        # vida de objeto alien no puedo ser menor a 0
        if self._health >= 1:
            self._health = self._health - 1
    
    @property
    def is_alive(self):
        if self._health > 0:
            return True
        else:
            return False
    
    def teleport(self, value_x, value_y):
        self.x_coordinate = value_x
        self.y_coordinate = value_y

    @property
    def collision_detection(self):
        return self._hited
    
    @collision_detection.setter
    def collision_detection(self, punto_de_impacto):
        if isinstance (punto_de_impacto, Proyectil):
            if punto_de_impacto[0] == self._x_coordinate and\
                punto_de_impacto[1] == self._y_coordinate:
                self._hited = True
            else:
                self._hited = False
                #print("No ha recibido impacto.")
    
    @property
    def arma(self):
        return self._arma
    
    @arma.setter
    def arma(self, arma):
        if isinstance(arma, Arma):
            self._arma = arma
        else:
            self._arma = None
    
    @property
    def num_ID(self):
        return self._num_ID
    
    @num_ID.setter
    def num_ID(self, num):
        if isinstance(num, int):
            self._num_ID = num
        else:
            return False