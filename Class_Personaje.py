from Configuraciones import *
import pygame as py
from Class_enemigo import Enemigo
from Class_box import box
from Class_disparo import disparo

class Personaje:
    def __init__(self, animaciones, tamaño, pos_x, pos_y, velocidad,vida,cantidad_telarañas,puntaje,pantalla="") -> None:
        self.animaciones = animaciones
        reescalar_imagenes(self.animaciones, *tamaño)
        self.rectangulo_principal = self.animaciones["Quieto"][0].get_rect()
        
        self.puntaje = puntaje
        self.vida = vida
        self.cant_telarañas = cantidad_telarañas
        self.rectangulo_principal.x = pos_x
        self.rectangulo_principal.y = pos_y
        self.rectangulo_principal_derecha = py.Rect(self.rectangulo_principal.right -10,self.rectangulo_principal.top,10,50)
        self.rectangulo_principal_derecha_golpe = py.Rect(self.rectangulo_principal.right +40,self.rectangulo_principal.top,10,50)
        self.rectangulo_principal_abajo = py.Rect(self.rectangulo_principal.left,self.rectangulo_principal.bottom-12,60,10)
        self.rectangulo_principal_izquierda = py.Rect(self.rectangulo_principal.left,self.rectangulo_principal.top,10,50)
        self.rectangulo_principal_izquierda_golpe = py.Rect(self.rectangulo_principal.left-40,self.rectangulo_principal.top,10,50)
        self.velocidad = velocidad
       
        self.esta_muerto = False

        self.ultimo_movimiento = ""

        self.que_hace = "Quieto"
        self.contador_pasos = 0
        self.animacion_actual = self.animaciones["golpea_derecha"]

        self.desplazamiento_y = 0
        self.potencia_salto = -20
        self.limite_velocidad_salto = 15
        self.gravedad = 1
        self.esta_saltando =False
        self.esta_cayendo = False
        self.ya_colisiono_electro= False
        self.habilidad_especial = False
        self.tiempo_habilidad_especial = 10000 #10 segundos
        self.tiempo_anterior = 0

        self.lista_proyectiles = []

    
    def actualizar(self, pantalla, piso):
        if self.esta_muerto == False:
            tiempo_actual= py.time.get_ticks()
            if tiempo_actual > self.tiempo_anterior + self.tiempo_habilidad_especial:
                self.habilidad_especial = False
            accion = ""
            if self.habilidad_especial == True:
                match self.que_hace:
                    case "Derecha":
                        accion = "super_derecha"
                    case "Izquierda":
                        accion = "super_izquierda"
                    case "Quieto":
                        accion = "super_quieto"
                    case "Salta":
                        accion = "super_salta"
                self.animacion_actual = self.animaciones[accion]
            if self.vida ==0 :
                self.animacion_actual = self.animaciones["derrotado"]
                self.esta_muerto = True
            else:
                self.animacion_actual = self.animaciones[self.que_hace]
            
            match self.que_hace:
                case "Derecha":
                    if not self.esta_saltando and self.animacion_actual != self.animaciones["derrotado"]:
                        #self.animacion_actual  = self.animaciones["Derecha"]
                        self.animar(pantalla)
                    self.caminar(pantalla)

                case "Izquierda":
                    if not self.esta_saltando and self.animacion_actual != self.animaciones["derrotado"]:
                        #self.animacion_actual  = self.animaciones["Izquierda"]
                        self.animar(pantalla)
                    self.caminar(pantalla)

                case "Quieto":
                    if not self.esta_saltando and self.animacion_actual != self.animaciones["derrotado"]:
                        #self.animacion_actual  = self.animaciones["Quieto"]
                        self.animar(pantalla)
                case "Quieto_izquierda":
                    if not self.esta_saltando and self.animacion_actual != self.animaciones["derrotado"]:
                        #self.animacion_actual  = self.animaciones["Quieto"]
                        self.animar(pantalla)
                case "golpea_izquierda":
                    if not self.esta_saltando and self.animacion_actual != self.animaciones["derrotado"]:
                        #self.animacion_actual  = self.animaciones["Quieto"]
                        self.animar(pantalla)
                case "golpea_derecha":
                    if not self.esta_saltando and self.animacion_actual != self.animaciones["derrotado"]:
                        #self.animacion_actual  = self.animaciones["Quieto"]
                        self.animar(pantalla)
                case "Salta":
                    if not self.esta_saltando and self.animacion_actual != self.animaciones["derrotado"]:
                        self.esta_saltando = True
                        self.desplazamiento_y = self.potencia_salto 
                #case "derrotado":
            #    self.animar(pantalla)
                
                    #if self.esta_cayendo ==True:
                    #    self.esta_cayendo = True
                        #self.animacion_actual  = self.animaciones["cae"]
                        #self.animar(pantalla)
        
        else:
            pantalla.blit(self.animaciones["derrotado"][0], self.rectangulo_principal)

        self.actualizar_proyectiles(pantalla)
        self.aplicar_gravedad(pantalla, piso)
        #self.animacion_actual = self.animaciones["cae"]

    def animar(self, pantalla):
        largo = len(self.animacion_actual)
        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        
        pantalla.blit(self.animacion_actual[self.contador_pasos], self.rectangulo_principal)
        #pantalla.blit(self.animacion_actual[self.contador_pasos], self.rectangulo_principal_derecha)
        
        self.contador_pasos += 1


    def caminar(self, pantalla):
        velocidad_actual = self.velocidad
        if self.que_hace == "Izquierda" and self.vida != 0:
            velocidad_actual *= -1
            
        
        nueva_x = self.rectangulo_principal.x + velocidad_actual
        
        if nueva_x >= 0 and nueva_x <= pantalla.get_width() - self.rectangulo_principal.width and self.vida != 0:
            self.rectangulo_principal.x += velocidad_actual
        
            self.rectangulo_principal_derecha.x += velocidad_actual
            self.rectangulo_principal_abajo.x += velocidad_actual
            self.rectangulo_principal_izquierda.x += velocidad_actual
            self.rectangulo_principal_izquierda_golpe.x += velocidad_actual
            self.rectangulo_principal_derecha_golpe.x += velocidad_actual


            
            
    
    def aplicar_gravedad(self, pantalla, plataformas):
        if self.esta_saltando and self.esta_muerto == False:
            self.animar(pantalla)
            self.rectangulo_principal.y += self.desplazamiento_y
            self.rectangulo_principal_derecha.y += self.desplazamiento_y
            self.rectangulo_principal_abajo.y += self.desplazamiento_y
            self.rectangulo_principal_izquierda.y += self.desplazamiento_y
            self.rectangulo_principal_izquierda_golpe.y += self.desplazamiento_y
            self.rectangulo_principal_derecha_golpe.y += self.desplazamiento_y
            
                
            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_salto:
                self.desplazamiento_y += self.gravedad
                self.animacion_actual  = self.animaciones["cae"]
                
                
                
                
            
        for piso in plataformas:
            if self.rectangulo_principal_abajo.colliderect(piso["rectangulo"]):            
                self.desplazamiento_y = 0
                self.esta_saltando = False
                #self.esta_cayendo = False
                
                self.rectangulo_principal_abajo.bottom = piso["rectangulo"].top
                self.rectangulo_principal.bottom = piso["rectangulo"].top
                self.rectangulo_principal_derecha.bottom = piso["rectangulo"].top
                self.rectangulo_principal_izquierda.bottom = piso["rectangulo"].top
                self.rectangulo_principal_izquierda_golpe.bottom = piso["rectangulo"].top
                self.rectangulo_principal_derecha_golpe.bottom = piso["rectangulo"].top
                break
            else:
                self.esta_saltando = True
                #self.esta_cayendo = True

    def verificar_colision_enemigo(self,lista_enemigos:list["Enemigo"], pantalla):
        #velocidad_actual = self.velocidad
        
        for enemigo in lista_enemigos:
            if self.rectangulo_principal_derecha.colliderect(enemigo.rectangulo_principal) and enemigo.animacion_actual != enemigo.animaciones["derrotado"] and self.vida != 0:
                self.vida =self.vida - 5
                self.rectangulo_principal.x = self.rectangulo_principal.x - 80
                self.rectangulo_principal_abajo.x = self.rectangulo_principal_abajo.x - 80
                self.rectangulo_principal_derecha.x = self.rectangulo_principal_derecha.x - 80
                self.rectangulo_principal_izquierda.x = self.rectangulo_principal_izquierda.x - 80
                self.rectangulo_principal_izquierda_golpe.x = self.rectangulo_principal_izquierda_golpe.x - 80
                self.rectangulo_principal_derecha_golpe.x = self.rectangulo_principal_derecha_golpe.x - 80           
                #enemigo.rectangulo_principal.y = 550            
                #enemigo.muriendo = True
            if self.rectangulo_principal_izquierda.colliderect(enemigo.rectangulo_principal) and enemigo.animacion_actual != enemigo.animaciones["derrotado"] and self.vida != 0:
                self.vida =self.vida - 5
                self.rectangulo_principal.x = self.rectangulo_principal.x + 80
                self.rectangulo_principal_abajo.x = self.rectangulo_principal_abajo.x + 80
                self.rectangulo_principal_derecha.x = self.rectangulo_principal_derecha.x + 80
                self.rectangulo_principal_izquierda.x = self.rectangulo_principal_izquierda.x + 80
                self.rectangulo_principal_izquierda_golpe.x = self.rectangulo_principal_izquierda_golpe.x + 80
                self.rectangulo_principal_derecha_golpe.x = self.rectangulo_principal_derecha_golpe.x + 80    
            if enemigo.animacion_actual == enemigo.animaciones["derrotado"]:
                self.vida = self.vida

    def verificar_colision_enemigo_dos(self,enemigo,pantalla):
        if self.rectangulo_principal_izquierda.colliderect(enemigo.rectangulo_principal) and enemigo.animacion_actual != enemigo.animaciones["derrotado"] and self.vida != 0:
            self.vida =self.vida - 5
            self.rectangulo_principal.x = self.rectangulo_principal.x + 80
            self.rectangulo_principal_abajo.x = self.rectangulo_principal_abajo.x + 80
            self.rectangulo_principal_derecha.x = self.rectangulo_principal_derecha.x + 80
            self.rectangulo_principal_izquierda.x = self.rectangulo_principal_izquierda.x + 80 
            self.rectangulo_principal_izquierda_golpe.x = self.rectangulo_principal_izquierda_golpe.x + 80
            self.rectangulo_principal_derecha_golpe.x = self.rectangulo_principal_derecha_golpe.x + 80
            self.puntaje -= 20  
        if self.rectangulo_principal_derecha.colliderect(enemigo.rectangulo_principal) and enemigo.animacion_actual != enemigo.animaciones["derrotado"] and self.vida != 0:
            self.vida =self.vida - 5
            self.rectangulo_principal.x = self.rectangulo_principal.x - 80
            self.rectangulo_principal_derecha.x = self.rectangulo_principal_derecha.x - 80
            self.rectangulo_principal_abajo.x = self.rectangulo_principal_abajo.x - 80
            self.rectangulo_principal_izquierda.x = self.rectangulo_principal_izquierda.x - 80
            self.rectangulo_principal_izquierda_golpe.x = self.rectangulo_principal_izquierda_golpe.x - 80
            self.rectangulo_principal_derecha_golpe.x = self.rectangulo_principal_derecha_golpe.x - 80   
            self.puntaje -= 20
        
                
        if enemigo.animacion_actual == enemigo.animaciones["derrotado"]:
            self.vida = self.vida

    #def verificar_estado_spiderman(self,pantalla):
    #    if self.vida == 0:
    #        self.animacion_actual  = self.animaciones["derrotado"]
            

    def verificar_colision_activa_disparo(self,zona_activacion,pos_x,pos_y,villano,pantalla):
        if self.ya_colisiono_electro==False:
            if self.rectangulo_principal.colliderect(zona_activacion["rectangulo"]):
                villano.disparar(pos_x,pos_y)
                
                if villano.rectangulo_principal.x == self.rectangulo_principal.x and villano.rectangulo_principal.y >600:
                    pantalla.blit(electro_derrotado, villano.rectangulo_principal)
                    self.ya_colisiono_electro==True
                
                    
        
            
    def romper_bloque(self,lista_plataformas,flor):
        for plataforma in lista_plataformas:
            if plataforma["premio"]==True:
                if self.rectangulo_principal.colliderect(plataforma["rectangulo"]):
                    flor["descubierta"] = True
                    plataforma["premio"] = False
    
    def verificar_colision_simbionte(self,simbionte):
        if self.rectangulo_principal.colliderect(simbionte["rectangulo"]):
            self.habilidad_especial = True


    def golpear(self):
        if self.que_hace == "Derecha" or self.que_hace =="Quieto":
            self.animacion_actual == "golpea_derecha"
        if self.que_hace == "Izquierda" or self.que_hace =="Quieto_izquierda":
            self.animacion_actual == "golpea_izquierda"
    def lanzar_telaraña(self):
        x = None
        margen = 47
        
        y = self.rectangulo_principal.centery + 10
        if self.que_hace == "Derecha" or self.que_hace =="Quieto":
            x = self.rectangulo_principal.right - margen
            vel_disparo = 20
            
            #self.animacion_actual = self.animaciones["dispara_derecha"]
        if self.que_hace == "Izquierda":
            x = self.rectangulo_principal.left - 20 + margen
            vel_disparo = 20
        if self.que_hace == "Quieto_izquierda":
            x = self.rectangulo_principal.left - 20 + margen
            vel_disparo = 20
        
            #self.animacion_actual = self.animaciones["dispara_izquierda"]
        if x is not None:
            self.lista_proyectiles.append(disparo(x,y,self.que_hace,vel_disparo,r"spiderman_game\Recursos\spider-man\telaraña.png"))

    def actualizar_proyectiles(self,pantalla):
        i = 0
        while i < len(self.lista_proyectiles):
            telaraña = self.lista_proyectiles[i]
            telaraña.actualizar(pantalla)
            
            if telaraña.rectangulo.centerx < 0 or telaraña.rectangulo.centerx > pantalla.get_width():
                self.lista_proyectiles.pop(i)
                i-= 1
            i += 1

    #DISPARO COLISION ENEMIGO
    def colision_telaraña(self,lista_enemigos:list["Enemigo"],pantalla):
        i = 0
        while i < len(self.lista_proyectiles):
            telaraña = self.lista_proyectiles[i]
            telaraña.actualizar(pantalla)
            for enemigo in lista_enemigos:
                if telaraña.rectangulo.colliderect(enemigo.rectangulo_principal) and enemigo.vida != 0:
                    enemigo.vida = enemigo.vida - 5
                    self.lista_proyectiles.pop(i)
                    if enemigo.vida <= 0:
                        enemigo.rectangulo_principal.y = enemigo.posicion_y_muerte
                        enemigo.animacion_actual = enemigo.animaciones["derrotado"]
                        i-= 1
                        if enemigo.animacion_actual == enemigo.animaciones["derrotado"]:
                            enemigo.vida = 0
            i += 1
    #def gastar_telaraña(self,pantalla,color_texto,color_fondo,fuente):
    #    cantidad_telarañas = self.cant_telarañas
    #    i = 1
    #    texto_telarañas = fuente.render(str(cantidad_telarañas),False,color_texto,color_fondo)
    #    pantalla.blit(texto_telarañas,(100,60))
        

    
'''
Caracteristicas
rectangulo
tamaño
velocidad
contador_pasos
que_hace
superficie

Acciones:
caminar
animar
actualizar_pantalla

'''