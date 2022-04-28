from tokenize import Triple
from alien import Alien
import random

from canon_de_protones import Canon
from granada_antimateria import Granada
from pistola_laser import Pistola
from proyectil import Proyectil

"""clase main en que se desarrollan las acciones de juego"""
class Juego():

    def __init__(self):
        
        coordenada_x = random.randint(0,15)
        coordenada_y = random.randint(0,15)
        self._armas = [] #lista de objetos armas
        self.attack = False #refiere a ataque de aliens

        # asignan posiciones arbitrarias
        alien_start_positions = [(4,7), (3,0)]
        # crea lista de objetos aliens
        self.aliens = self.new_aliens_collection\
            (alien_start_positions)

        # asigna numero de ID a aliens registrados
        for indice in range(0,len(self.aliens)):
            self.aliens[indice].num_ID = indice

        # lista incluye elemento = None
        # tal que se puede no tener arma
        self.armas = [None, Canon(), Granada(), Pistola()]

        # asigna armas a obejtos de lista aliens
        for alien in self.aliens:
            alien.arma = random.choice(self.armas)

        # no aplica getter
        # imprime atributo supuestamente privado
        print(alien._health)
        
        # llama a funcion donde comienza interacion de juego
        #self.battlefield()
    
    """ funcion que acapara visualizacion de juego """
    def battlefield(self):

        # indica la escena de juego
        n = -1 
        # crea objeto proyectil asociado a disparo de arma
        self.proyectil = Proyectil()
        # ciclo acaba cuando quede un objeto alien en lista
        # analogia:objeto alien fuera de lista -> alien caido
        while len(self.aliens) != 1:
            for alien in self.aliens:

                n = n + 1
                print("_____________")
                print("Escena ", n)
                print("Alien ", alien.num_ID )
                print("En posicion: ",\
                    alien.x_coordinate, alien.y_coordinate)
                teletransportar = random.choice([True,False])
                if teletransportar is True:
                    alien.x_coordinate = random.randint(0,15)
                    alien.y_coordinate = random.randint(0,15)
                    print(f"Alien {alien.num_ID} se teletrans\
porta a posicion:", alien.x_coordinate, alien.y_coordinate)
                if alien.arma != None:
                    print("Arma equipada: ",alien.arma.nombre)
                else:
                    print("Arma equipada: None")

                """ 'self.attack' refiere a riesgo de ser
                atacado, mientras que 'self.proyectil.impact'
                , de ser 'True', refiere a un ataque seguro"""
                if self.attack is True:
                    print("Riesgo de ser atacado: ",\
                        self.attack)
                if self.proyectil.impact is True:
                    # alien pierde vida(s) respectiva(s)
                    self.alien_hited(alien)
                else:
                    if self.attack is True:
                        alien.collision_detection = \
                            self.proyectil.destination
                        # si existe coincidencia de puntos
                        # tal que colision es Verdadera
                        if alien.hited is True:
                            self.alien_hited(alien)
                    else:
                        pass
                # si alien tiene arma y esta vivo
                # realiza ataque a enemigo
                if alien.arma != None and alien.is_alive \
                    is True:
                    print(f"Alien {alien.num_ID} \
prepara ataque.")
                    self.attack = True
                    # dirigue a funcion que prepara ataque
                    self.prepare_attack(alien)
                # alien no prepara ataque
                # tal que no tiene arma o ha caido
                else:
                    self.attack = False
                    self.proyectil = Proyectil()
                alien.arma = random.choice(self.armas)

    def alien_hited(self, alien):

        for damage in range(0, self.proyectil.damage):
            alien.hit()
        print("Ha recibido impacto")
        print("Vidas restantes: ",alien.health)
        if alien.is_alive is False:
            print("Alien ", alien.num_ID,\
                "ha caido." )
            self.aliens.remove(alien)
            self.proyectil = Proyectil()

    def prepare_attack(self, alien):

        # exactitud de disparo dependera de la clase de arma
        # cada clase de arma deja daño en particular
        # arma de mayor exactitud en disparo, menor daño
        if alien.arma.precision is True:
            print("Disparo con maxima exactitud")
            print("Daño a rival inminente")
            print("Resta",alien.arma.damage,"de vida a rival")
            self.proyectil.impact = True
        else:
            self.proyectil.destination = \
                [random.randint(0,15),\
                    random.randint(0,15)]
            print("Exactitud de disparo es azarosa.")
            print("Alien {0} abre fuego a punto {1}"\
            .format(alien.num_ID, self.proyectil.destination))
            self.proyectil.impact = False
        self.proyectil.damage = alien.arma.damage


    def new_aliens_collection(self, alien_start_positions):

        # alien_start_positions son coordenadas clase list
        aliens = []
        for coordenada in alien_start_positions:
            aliens.append(Alien(coordenada[0],coordenada[1]))

        # retorna lista de objetos clase alien
        return aliens
    
    def total_aliens_created(self):
        return print(len(self.aliens))



juego = Juego()