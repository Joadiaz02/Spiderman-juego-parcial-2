from Configuraciones import *
from Class_disparo import * 
class Enemigo:
    #lizard = Enemigo(diccionario_animaciones_lizard,1200,535,"izquierda",primera_tope_izquierda,primera_tope_derecha,PANTALLA)
    def __init__(self, animaciones, pos_x,pos_y,accion_inicial,tope_uno,tope_dos,vida,posicion_y_muerte,pantalla) -> None:
        self.animaciones = animaciones
        reescalar_imagenes(self.animaciones, 120,100)
        self.rectangulo_principal = self.animaciones[accion_inicial][0].get_rect()
        self.rectangulo_principal.x = pos_x
        self.rectangulo_principal.y = pos_y
        self.tope_uno= tope_uno
        self.tope_dos = tope_dos
        self.esta_muerto = False
        self.movimiento_inicial = False
        self.pasos = 0
        self.vida = vida
        self.que_hace= "Derecha"
        self.animacion_actual = self.animaciones[accion_inicial]
        self.muriendo = False       
        self.va_izquierda = True
        self.va_derecha = False
        self.posicion_y_muerte = posicion_y_muerte
        self.primera_tope_izquierda = py.draw.rect(pantalla,"red",(215,580,10,40),3)  
        self.primera_tope_derecha = py.draw.rect(pantalla,"red",(1190,580,10,40),3) 
        self.lista_proyectiles = []                           

    def avanzar_greengoblin(self):
        if self.movimiento_inicial == False and self.animacion_actual != self.animaciones["derrotado"]:
            self.animacion_actual = self.animaciones["sube"]
            self.rectangulo_principal.y -= 8
        if self.rectangulo_principal.colliderect(self.tope_uno["rectangulo"])and self.animacion_actual != self.animaciones["derrotado"] :
            self.movimiento_inicial = True
        if self.movimiento_inicial == True:
            self.animacion_actual = self.animaciones["sube"]
            self.rectangulo_principal.y += 8
        if self.rectangulo_principal.colliderect(self.tope_dos["rectangulo"])and self.animacion_actual != self.animaciones["derrotado"] :
            self.movimiento_inicial = False
        
        if  self.vida<=0:
            self.rectangulo_principal.y +=10
        
    
    def avanzar(self):
        if self.movimiento_inicial == False and self.animacion_actual != self.animaciones["derrotado"]:
            self.animacion_actual = self.animaciones["izquierda"]
            self.rectangulo_principal.x -= 8
        if self.rectangulo_principal.colliderect(self.tope_uno["rectangulo"])and self.animacion_actual != self.animaciones["derrotado"] :
            self.movimiento_inicial = True
        if self.movimiento_inicial == True:
            self.animacion_actual = self.animaciones["derecha"]
            self.rectangulo_principal.x += 8
        if self.rectangulo_principal.colliderect(self.tope_dos["rectangulo"])and self.animacion_actual != self.animaciones["derrotado"] :
            self.movimiento_inicial = False
        
        if  self.vida<=0 and self.movimiento_inicial== False:
            self.rectangulo_principal.x +=0
        if self.vida <=0 and self.movimiento_inicial == True:
            self.rectangulo_principal.x -=8
    
    def animar(self, pantalla):
        if self.vida != 0:
            largo = len(self.animacion_actual)

            if self.pasos >= largo:
                self.pasos = 0

            pantalla.blit(self.animacion_actual[self.pasos], self.rectangulo_principal)
            self.pasos += 1

            if self.muriendo and self.pasos == largo:
                self.esta_muerto = True
            if self.esta_muerto == True:
                self.animacion_actual = self.animaciones["derrotado"]
            
        if self.vida ==0:
            self.animacion_actual = self.animaciones["derrotado"]
            pantalla.blit(self.animacion_actual[0], self.rectangulo_principal)
            
    def actualizar(self, pantalla):
        if self.esta_muerto == False:
            self.animar(pantalla)
            self.avanzar()
            self.actualizar_proyectiles_simbiontes(pantalla)
        #if self.vida == 0:
        #    self.animacion_actual = self.animaciones["derrotado"]

    def actualizar_greengoblin(self, pantalla):
        if self.esta_muerto == False:
            self.animar(pantalla)
            self.avanzar_greengoblin()
            self.actualizar_proyectiles_simbiontes(pantalla)

    def actualizar_dos(self, pantalla):
        if self.esta_muerto == False:
            self.animar(pantalla)

    def disparar(self,pos_x,pos_y):
        self.animacion_actual = self.animaciones["disparo"]
        self.rectangulo_disparo = self.animaciones["disparo"][0].get_rect()
        self.rectangulo_principal.x -=10
        
        #pantalla.blit(self.animacion_actual,self.rectangulo_disparo)


    def lanzar_simbionte(self):
        x = None
        margen = 47
        
        y = self.rectangulo_principal.centery - 10
        if self.movimiento_inicial == True:
            x = self.rectangulo_principal.right - margen
            vel_disparo = 30
            self.que_hace = "Derecha"
            #self.animacion_actual = self.animaciones["dispara_derecha"]
        if self.movimiento_inicial == False:
            x = self.rectangulo_principal.left - 20 + margen
            vel_disparo = 30
            self.que_hace = "Izquierda"
        
        
            #self.animacion_actual = self.animaciones["dispara_izquierda"]
        if x is not None:
            self.lista_proyectiles.append(disparo(x,y,self.que_hace,vel_disparo,r"spiderman_game\Recursos\objetos\simbionte-3.png"))

    def hobgoblin_lanza_granada(self):
        x = None
        margen = 47
        
        y = self.rectangulo_principal.centery - 10
        if self.movimiento_inicial == True:
            x = self.rectangulo_principal.right - margen
            vel_disparo = 30
            self.que_hace = "Derecha"
            #self.animacion_actual = self.animaciones["dispara_derecha"]
        if self.movimiento_inicial == False:
            x = self.rectangulo_principal.left - 20 + margen
            vel_disparo = 30
            self.que_hace = "Izquierda"
        
        
            #self.animacion_actual = self.animaciones["dispara_izquierda"]
        if x is not None:
            self.lista_proyectiles.append(disparo(x,y,"abajo",vel_disparo,r"spiderman_game\Recursos\hob-goblin\granada.png"))
    
    def greengoblin_lanza_granada(self):
        x = None
        margen = 47
        
        y = self.rectangulo_principal.centery - 10
        if self.movimiento_inicial == True:
            x = self.rectangulo_principal.right - margen
            vel_disparo = 30
            self.que_hace = "Derecha"
            #self.animacion_actual = self.animaciones["dispara_derecha"]
        if self.movimiento_inicial == False:
            x = self.rectangulo_principal.left - 20 + margen
            vel_disparo = 30
            self.que_hace = "Izquierda"
        
        
            #self.animacion_actual = self.animaciones["dispara_izquierda"]
        if x is not None:
            self.lista_proyectiles.append(disparo(x,y,"Derecha",vel_disparo,r"spiderman_game\Recursos\green-goblin\granada.png"))
    
    
    def actualizar_proyectiles_simbiontes(self,pantalla):
        i = 0
        while i < len(self.lista_proyectiles):
            telaraña = self.lista_proyectiles[i]
            telaraña.actualizar(pantalla)
            
            if telaraña.rectangulo.centerx < 0 or telaraña.rectangulo.centerx > pantalla.get_width():
                self.lista_proyectiles.pop(i)
                i-= 1
            i += 1

    def colision_simbionte(self,personaje,pantalla):
        i = 0
        while i < len(self.lista_proyectiles):
            telaraña = self.lista_proyectiles[i]
            telaraña.actualizar(pantalla)
            
            if telaraña.rectangulo.colliderect(personaje.rectangulo_principal) and personaje.vida != 0:
                personaje.vida = personaje.vida - 5
                self.lista_proyectiles.pop(i)
                if personaje.vida == 0:
                    personaje.rectangulo_principal.y = personaje.posicion_y_muerte
                    #    personaje.animacion_actual = personaje.animaciones["derrotado"]
                    #    i-= 1
                    #    if personaje.animacion_actual == personaje.animaciones["derrotado"]:
                    #        personaje.vida = 0
            i += 1