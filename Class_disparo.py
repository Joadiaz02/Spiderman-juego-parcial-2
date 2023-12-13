import pygame as py
from Class_Personaje import *
class disparo:
    def __init__(self, x, y, direccion,vel_disparo,path):
        self.superficie = py.image.load(path)
        self.superficie = py.transform.scale(self.superficie,(20,20))
        self.rectangulo = self.superficie.get_rect()
        self.rectangulo.x = x
        self.rectangulo.centery = y
        self.vel_disparo = vel_disparo
        self.direccion = direccion
        
    def actualizar(self, pantalla):
        if self.direccion == "Derecha" or self.direccion == "Quieto":
            self.rectangulo.x += self.vel_disparo
            #self.animacion_actual = self.animaciones["dispara_derecha"]
        elif self.direccion == "Izquierda":
            self.rectangulo.x -= self.vel_disparo
        elif self.direccion == "Quieto_izquierda":
            self.rectangulo.x -= self.vel_disparo
        elif self.direccion == "abajo":
            self.rectangulo.y += self.vel_disparo
            #.animacion_actual = Personaje.animaciones["dispara_derecha"]
        pantalla.blit(self.superficie,self.rectangulo)