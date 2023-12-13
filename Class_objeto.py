from Configuraciones import *
import pygame as py
import random 
class Objeto:
    def __init__(self, objetos,tipo,pos_x,pos_y) -> None:
        self.objetos = objetos
        #self.imagen = py.image.load("spiderman_game\Recursos\objetos\corazon.png")
        reescalar_imagenes(self.objetos, 50,50)
        self.rectangulo_principal = self.objetos[tipo][0].get_rect()
        self.rectangulo_principal.x = pos_x
        self.rectangulo_principal.y = pos_y
        self.tipo = tipo
        self.numero = random.randint(0,4)
        self.agarrado = False


    
    def imprimir_objeto(self,pantalla):
        match self.numero:
            case 1:
                #objeto = py.image.load(self.imagen)
                #objeto = py.transform.scale(self.objetos[self.tipo],self.rectangulo_principal)
                self.rectangulo_principal.x = 1000
                self.rectangulo_principal.y = 500 
                pantalla.blit(self.objetos[self.tipo][0],self.rectangulo_principal)
            case 2:
                #objeto = py.image.load(self.imagen)
                #objeto = py.transform.scale(objeto,(50,50))
                self.rectangulo_principal.x = 300
                self.rectangulo_principal.y = 444 
                pantalla.blit(self.objetos[self.tipo][0],self.rectangulo_principal)
            case 3:
                #objeto = py.image.load(self.imagen)
                #objeto = py.transform.scale(objeto,(50,50))
                self.rectangulo_principal.x = 1000
                self.rectangulo_principal.y = 200
                pantalla.blit(self.objetos[self.tipo][0],self.rectangulo_principal)
            case 4:
                #objeto = py.image.load(self.imagen)
                #objeto = py.transform.scale(objeto,(50,50))
                self.rectangulo_principal.x = 200
                self.rectangulo_principal.y = 1000 
                pantalla.blit(self.objetos[self.tipo][0],self.rectangulo_principal)



    
    def blitear_objeto(self,pantalla):
        if self.agarrado == False:
            pantalla.blit(self.objetos[self.tipo][0],self.rectangulo_principal)
        