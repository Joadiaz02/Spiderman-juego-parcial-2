import pygame as py
from pygame.locals import *

from Class_nivel_uno import NivelUno 
from Class_nivel_dos import NivelDos
from Class_nivel_tres import NivelTres

class Manejador_niveles:
    def __init__(self,PANTALLA):
        self._slave = PANTALLA
        self.niveles = {"nivel_uno":NivelUno, "nivel_dos":NivelDos,"nivel_tres": NivelTres}


    def get_nivel(self,nombre_nivel):
        return self.niveles[nombre_nivel](self._slave)