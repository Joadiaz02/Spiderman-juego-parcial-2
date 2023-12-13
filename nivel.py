import pygame as py
import sqlite3
from pygame.locals import *
from os import system
system("cls")
from Modo import *
from funcion_plataforma import *
from Class_Personaje import Personaje
from Configuraciones import *
import time
from archivos.funciones import *
from funcion_tiempo import *

class Nivel:
    def __init__(self,pantalla,nivel,personaje_principal,jefe,villano_uno,villano_dos,imagen_fondo,color_uno,color_dos,color_tres,color_cuatro,color_cinco,color_seis,color_siete,color_ocho,primer_objeto,segundo_objeto,tercer_objeto,scorpion_esta_muerto,scorpion_dos_esta_muerto,jefe_esta_muerto,bandera_aparece_jefe,bandera_disparo,tiempo_ultimo_disparo,que_hace,aux,flag,fuente,eje_y,diccionario_black,lista_enemigos,bandera_pausa,tiempo,jefe_dos="",bandera_aparece_greengoblin="",greengoblin_esta_muerto="",tiempo_ultimo_disparo_greengoblin =""):
        self._slave = pantalla
        self.jugador = personaje_principal
        self.img_fondo = imagen_fondo
        self.jefe = jefe
        self.villano_uno = villano_uno
        self.villano_dos = villano_dos
        self.color_uno = color_uno
        self.color_dos = color_dos
        self.color_tres = color_tres
        self.color_cuatro = color_cuatro
        self.color_cinco = color_cinco
        self.color_seis = color_seis
        self.color_siete = color_siete
        self.color_ocho = color_ocho
        self.primer_objeto = primer_objeto
        self.segundo_objeto = segundo_objeto
        self.tercer_objeto = tercer_objeto
        self.lista_enemigos = lista_enemigos
        self.scorpion_esta_muerto = scorpion_esta_muerto
        self.scorpion_dos_esta_muerto = scorpion_dos_esta_muerto
        self.jefe_esta_muerto = jefe_esta_muerto 
        self.bandera_aparece_jefe = bandera_aparece_jefe
        self.bandera_disparo = bandera_disparo
        self.tiempo_ultimo_disparo = tiempo_ultimo_disparo
        self.que_hace = que_hace
        self.aux = aux
        self.flag = flag
        self.fuente = fuente
        self.eje_y = eje_y
        self.nivel = nivel
        self.diccionario_black = diccionario_black
        self.bandera_pausa = bandera_pausa
        self.bandera_aparece_greengoblin = bandera_aparece_greengoblin
        self.greengoblin_esta_muerto = greengoblin_esta_muerto
        self.tiempo_ultimo_disparo_greengoblin = tiempo_ultimo_disparo_greengoblin
        self.jefe_dos = jefe_dos
        self.tiempo_milisegundos =0
        self.bandera_juego_iniciado = True
        self.bandera_juego_iniciado_dos = True
        self.bandera_juego_iniciado_tres = True
        self.bandera_ya_sumo_nivel_dos = False

        self.bandera_ya_sumo_nivel_tres = False
        
        self.bandera_ya_sumo_tiempo_uno = False
        self.bandera_ya_sumo_tiempo_dos = False
        self.bandera_ya_sumo_tiempo_tres = False
        self.tiempo =60
        self.tiempo_uno = 0
        self.tiempo_dos = py.time.get_ticks()
        self.ingreso_nombre= False
        
    def update_nivel(self,lista_eventos):
        for event in lista_eventos:
            if event.type == py.KEYDOWN:
                if event.key == py.K_TAB:
                    cambiar_modo()
        self.leer_inputs()
        self.actualizar_pantalla()

    
    def update(self,lista_eventos):
        py.init()
        #tiempo =0
        self._slave.blit(self.img_fondo,(0,0))
        partidas=lectura_partida_json()

        #suma_punatajes = lambda diccionario:  for diccionario in 
        if self.nivel =="nivel_dos" and self.bandera_ya_sumo_nivel_dos == False:
            self.jugador.puntaje = partidas["puntaje_nivel_uno"] + self.jugador.puntaje
            self.bandera_ya_sumo_nivel_dos = True
        if self.nivel == "nivel_tres" and self.bandera_ya_sumo_nivel_tres == False:
            self.jugador.puntaje =  partidas["puntaje_nivel_dos"] + self.jugador.puntaje
            self.bandera_ya_sumo_nivel_tres = True
        for event in lista_eventos:
            
            if event.type == py.KEYDOWN:
                if event.key == py.K_TAB:
                    cambiar_modo()
        teclas = py.key.get_pressed()

        if teclas[py.K_RIGHT] and self.jugador.animacion_actual != self.jugador.animaciones["derrotado"]:
            self.jugador.que_hace = "Derecha"
            self.bandera_disparo = True
            self.jugador.ultimo_movimiento = "Derecha"
        elif teclas[py.K_p] and self.bandera_pausa == False :
            self.bandera_pausa = True
        elif teclas[py.K_p] and self.bandera_pausa == True :
            self.bandera_pausa = False
        elif teclas[py.K_LEFT] and self.jugador.animacion_actual != self.jugador.animaciones["derrotado"]:
            self.jugador.que_hace = "Izquierda"
            self.bandera_disparo = True
            self.jugador.ultimo_movimiento = "Izquierda"
        elif(teclas[py.K_SPACE]) and self.jugador.animacion_actual != self.jugador.animaciones["derrotado"]:
            self.jugador.que_hace = "Salta"
            self.bandera_disparo = True
        elif self.jugador.animacion_actual != self.jugador.animaciones["derrotado"]:
            if self.jugador.ultimo_movimiento == "Derecha":
                self.jugador.que_hace = "Quieto"
            if self.jugador.ultimo_movimiento == "Izquierda":
                self.jugador.que_hace = "Quieto_izquierda"
            self.bandera_disparo = True
        fuente = self.fuente
        
        
        #TRAMPAS
        if self.nivel == "nivel_uno":
            trampa = crear_plataforma(self._slave,True,False,False,(120,50),1050,265,r"spiderman_game\Recursos\objetos\trampa.png")
            
        if self.nivel == "nivel_dos":
            trampa = crear_plataforma(self._slave,True,False,False,(180,20),540,308,r"spiderman_game\Recursos\objetos\trampa.png")
           
        if self.nivel == "nivel_tres":
            trampa = crear_plataforma(self._slave,True,False,False,(180,20),840,117,r"spiderman_game\Recursos\objetos\trampa.png")
           

        if self.jugador.rectangulo_principal.colliderect(trampa["rectangulo"]):
            self.jugador.rectangulo_principal.y += 100
            self.jugador.rectangulo_principal_abajo.y += 100
            self.jugador.rectangulo_principal_derecha.y += 100
            self.jugador.rectangulo_principal_izquierda.y += 100
            self.jugador.rectangulo_principal_izquierda_golpe.y += 100
            self.jugador.rectangulo_principal_derecha_golpe.y += 100
            self.jugador.puntaje -= 50
            self.jugador.vida = self.jugador.vida -20
            #resta(self.jugador.vida,20)
        
        #TIEMPO JUEGO
        if  self.bandera_pausa == False :
            #self.tiempo/1000
            self.tiempo_dos= py.time.get_ticks()
            if self.tiempo_dos > self.tiempo_uno + 1000:
                self.tiempo_uno = self.tiempo_dos
                self.tiempo = self.tiempo - 1
        contador = fuente.render("Tiempo : "+str(self.tiempo),True,self.color_uno,self.color_dos)
        self._slave.blit(contador,(550,20))

        #if self.bandera_pausa == False:
        #    for s in range (600000000,0,-1):
        #        tiempo = s /100
        #        tiempo = int(tiempo)
        #        contador = fuente.render("Tiempo : "+str(tiempo),True,self.color_uno,self.color_dos)
        #        self._slave.blit(contador,(550,20))
       
        #VIDA SPIDER-MAN
        
        texto_spiderman = fuente.render(str(self.jugador.vida),False,self.color_uno,self.color_dos)
        icono_spiderman = py.image.load(r"spiderman_game\Recursos\spider-man\vida-logo.png")
        icono_spiderman = py.transform.scale(icono_spiderman,(70,70))
        self._slave.blit(icono_spiderman,(20,30))
        self._slave.blit(texto_spiderman,(100,30))

        if self.bandera_pausa== True:
            logo_pausa = py.image.load(r"spiderman_game\Recursos\boton_pausa.png")
            logo_pausa = py.transform.scale(logo_pausa,(300,200))
            self._slave.blit(logo_pausa,(400,300))


        #CANTIDAD DE TELARAÑAS
        texto_cant_telarañas = fuente.render(str(self.jugador.cant_telarañas),False,self.color_uno,self.color_dos)
        icono_cant_telarañas = py.image.load(r"spiderman_game\Recursos\spider-man\telaraña.png")
        icono_cant_telarañas =  py.transform.scale(icono_cant_telarañas,(70,70))
        self._slave.blit(icono_cant_telarañas,(20,90))
        self._slave.blit(texto_cant_telarañas,(100,105))
        

        icono_cant_puntaje = py.image.load(r"spiderman_game\Recursos\fondos\score.png")
        icono_cant_puntaje =  py.transform.scale(icono_cant_puntaje,(70,40))
        self._slave.blit(icono_cant_puntaje,(20,150))
        puntaje = fuente.render(str(self.jugador.puntaje),True,self.color_uno,self.color_dos)
        self._slave.blit(puntaje,(100,150))
        
        tiempo_actual = py.time.get_ticks()
        teclas = py.key.get_pressed()
        
        if teclas[py.K_f] and self.bandera_disparo ==True and self.jugador.vida >0 and self.jugador.cant_telarañas !=0 and self.bandera_pausa == False:
            
            if self.jugador.que_hace  == "Derecha" or self.jugador.que_hace =="Quieto" and self.jugador.cant_telarañas !=0 :
                if tiempo_actual - self.tiempo_ultimo_disparo >= 500 :
                    self.jugador.lanzar_telaraña()
                    self.jugador.cant_telarañas = self.jugador.cant_telarañas - 1
                    self.tiempo_ultimo_disparo = tiempo_actual
            if self.jugador.que_hace  == "Izquierda" or self.jugador.ultimo_movimiento  == "Izquierda" :
                if tiempo_actual - self.tiempo_ultimo_disparo >= 500 and self.jugador.cant_telarañas !=0:
                    self.jugador.lanzar_telaraña()
                    self.jugador.cant_telarañas = self.jugador.cant_telarañas - 1
                    self.tiempo_ultimo_disparo = tiempo_actual
            if self.tercer_objeto.agarrado == True:
                if self.jugador.que_hace  == "Derecha" or self.jugador.que_hace =="Quieto" and self.jugador.cant_telarañas !=0 :
                    if tiempo_actual - self.tiempo_ultimo_disparo >= 200 :
                        self.jugador.lanzar_telaraña()
                        self.jugador.cant_telarañas = self.jugador.cant_telarañas - 1
                        self.tiempo_ultimo_disparo = tiempo_actual
                if self.jugador.que_hace  == "Izquierda" or self.jugador.ultimo_movimiento  == "Izquierda" :
                    if tiempo_actual - self.tiempo_ultimo_disparo >= 200 and self.jugador.cant_telarañas !=0:
                        self.jugador.lanzar_telaraña()
                        self.jugador.cant_telarañas = self.jugador.cant_telarañas - 1
                        self.tiempo_ultimo_disparo = tiempo_actual
        
        if teclas[py.K_j]:
                if self.jugador.ultimo_movimiento == "Derecha":
                    self.jugador.que_hace = "golpea_derecha"
                if self.jugador.ultimo_movimiento == "Izquierda":
                    self.jugador.que_hace = "golpea_izquierda"
                
                if self.jugador.rectangulo_principal_derecha_golpe.colliderect(self.villano_uno.rectangulo_principal) and self.villano_uno.vida >0 :
                    self.jugador.que_hace = "golpea_derecha"
                    self.villano_uno.vida = self.villano_uno.vida -5
                if self.jugador.rectangulo_principal_derecha_golpe.colliderect(self.villano_dos.rectangulo_principal) and self.villano_dos.vida >0:
                    self.jugador.que_hace = "golpea_derecha"
                    self.villano_dos.vida = self.villano_dos.vida -5
                if self.jugador.rectangulo_principal_derecha_golpe.colliderect(self.jefe.rectangulo_principal) and self.jefe.vida >0:
                    self.jugador.que_hace = "golpea_derecha"
                    self.jefe.vida = self.jefe.vida -5
                if self.jefe.animacion_actual == self.jefe.animaciones["derrotado"]:
                    self.jefe.vida = 0
                if self.jugador.rectangulo_principal_izquierda_golpe.colliderect(self.villano_uno.rectangulo_principal) and self.villano_uno.vida >0 :
                    self.jugador.que_hace = "golpea_izquierda"
                    self.villano_uno.vida = self.villano_uno.vida -5
                if self.jugador.rectangulo_principal_izquierda_golpe.colliderect(self.villano_dos.rectangulo_principal) and self.villano_dos.vida >0:
                    self.jugador.que_hace = "golpea_izquierda"
                    self.villano_dos.vida = self.villano_dos.vida -5
                if self.jugador.rectangulo_principal_izquierda_golpe.colliderect(self.jefe.rectangulo_principal) and self.jefe.vida >0:
                    self.jugador.que_hace = "golpea_izquierda"
                    self.jefe.vida = self.jefe.vida -5

        #POSICION MUERTE VILLANOS
        if self.villano_uno.vida <=0:
            self.villano_uno.rectangulo_principal.y = self.villano_uno.posicion_y_muerte
        if self.villano_dos.vida <=0:
            self.villano_dos.rectangulo_principal.y = self.villano_dos.posicion_y_muerte
        if self.jefe.vida <=0:
            self.jefe.rectangulo_principal.y = self.jefe.posicion_y_muerte
        
        #VIDA LIZARD
        if self.villano_uno.vida <= 0 and self.villano_dos.vida <=0 and self.bandera_aparece_jefe == True and self.nivel == "nivel_uno":
            texto_lizard = fuente.render(str(self.jefe.vida),False,self.color_tres,self.color_cuatro)
            icono_lizard = py.image.load(r"spiderman_game\Recursos\lizard\vida-lizard.png")
            icono_lizard = py.transform.scale(icono_lizard,(70,70))
            self._slave.blit(icono_lizard,(1000,20))
            self._slave.blit(texto_lizard,(920,30))
        #VIDA VENOM
        if self.villano_uno.vida <= 0 and self.villano_dos.vida <=0 and self.bandera_aparece_jefe == True and self.nivel == "nivel_dos":
            texto_venom = fuente.render(str(self.jefe.vida),False,self.color_cinco,self.color_uno)
            icono_venom = py.image.load(r"spiderman_game\Recursos\venom\venom-vida.png")
            icono_venom = py.transform.scale(icono_venom,(70,70))
            self._slave.blit(icono_venom,(1000,20))
            self._slave.blit(texto_venom,(920,30))
        
        #COLISIONES ENEMIGOS Y TELARAÑAS
        if self.villano_uno.vida > 0 :
            self.jugador.verificar_colision_enemigo_dos(self.villano_uno, self._slave)
        if self.villano_dos.vida >0 :
            self.jugador.verificar_colision_enemigo_dos(self.villano_dos, self._slave)
        if self.jefe.vida >0:
            self.jugador.verificar_colision_enemigo_dos(self.jefe,self._slave)
        if self.jefe.vida >0 and self.nivel == "nivel_tres":
            self.jugador.verificar_colision_enemigo_dos(self.jefe_dos,self._slave)
        if self.bandera_pausa == False:
            self.jugador.colision_telaraña(self.lista_enemigos,self._slave)
        
        
        
        
            self.villano_uno.actualizar(self._slave)
            self.villano_dos.actualizar(self._slave)
        if self.villano_uno.vida <=0 and self.scorpion_esta_muerto == False:
            self.jugador.puntaje +=250
            self.scorpion_esta_muerto = True
        if self.villano_dos.vida == 0 and self.scorpion_dos_esta_muerto == False:
            self.jugador.puntaje +=250
            self.scorpion_dos_esta_muerto = True
        if self.jefe.vida <= 0 and self.jefe_esta_muerto== False:
            self.jugador.puntaje += 1000
            self.jefe_esta_muerto = True
        if self.villano_uno.vida <= 0 and self.villano_dos.vida ==0:
            self.bandera_aparece_jefe = True
        if self.bandera_aparece_jefe == True and self.nivel == "nivel_uno" and self.bandera_pausa == False:
            self.jefe.actualizar(self._slave)
        
        
        tiempo_game_over = py.time.get_ticks()
        #TEWMPORIZADOR
        #tiempo_inicial = time.time()
        #duracion_temporizador = 6000
        #tiempo_final = tiempo_inicial + duracion_temporizador
        #while time.time()<= tiempo_final:
            #tiempo = int(tiempo_final - time.time())
            
            #contador = fuente.render("Tiempo : "+str(tiempo/100),True,self.color_uno,self.color_dos)
            #self._slave.blit(contador,(550,20))


        #CREANDO PLATAFORMAS
        if self.nivel == "nivel_uno":
            piso = crear_plataforma(self._slave,False,False,False, (1200,20), 216, 620, r"spiderman_game\Recursos\fondos\fondo-1.jpg")
            plataforma_invisible= plataforma_invisible = crear_plataforma(self._slave,False,False,False,(535,20),220,425,r"spiderman_game\Recursos\fondos\fondo-1.jpg")
            plataforma_invisible_2 = crear_plataforma(self._slave,False,False,False,(535,20),220,225,r"spiderman_game\Recursos\fondos\fondo-1.jpg")
            plataforma_invisible_3 = crear_plataforma(self._slave,False,False,False,(181,20),1014,425,r"mario-bros\Recursos\fondo.png")
            plataforma_invisible_4 = crear_plataforma(self._slave,False,False,False,(181,20),1014,225,r"mario-bros\Recursos\fondo.png")
        
            plataforma_movil_nivel_uno = crear_plataforma_movil(self._slave,True,False,True,(100,50),50,eje_y,r"spiderman_game\Recursos\fondos\planeador.png")
            plataformas= [piso, plataforma_invisible_2, plataforma_invisible,plataforma_invisible_3,plataforma_invisible_4,plataforma_movil_nivel_uno]
        
        if self.nivel == "nivel_dos":
            piso = crear_plataforma(self._slave,False,False,False, (820,20), 0, 470, r"spiderman_game\Recursos\fondos\fondo-1.jpg")
            plataforma_invisible = crear_plataforma(self._slave,False,False,False,(370,20),930,520,r"spiderman_game\Recursos\fondos\fondo-1.jpg")

            plataforma_invisible_2 = crear_plataforma(self._slave,False,False,False,(160,20),910,260,r"spiderman_game\Recursos\fondos\fondo-1.jpg")
            
            plataforma_invisible_3 = crear_plataforma(self._slave,False,False,False,(290,20),530,270,r"mario-bros\Recursos\fondo.png")
            plataforma_invisible_4 = crear_plataforma(self._slave,False,False,False,(300,20),50,270,r"mario-bros\Recursos\fondo.png")
            plataforma_diagonal_abajo = crear_plataforma(self._slave,False,False,False,(70,20),820,490,r"mario-bros\Recursos\fondo.png")
            plataforma_diagonal_abajo_dos = crear_plataforma(self._slave,False,False,False,(70,20),850,510,r"mario-bros\Recursos\fondo.png")
            plataforma_diagonal_arriba = crear_plataforma(self._slave,False,False,False,(70,10),1060,230,r"mario-bros\Recursos\fondo.png")
            plataforma_diagonal_arriba_dos = crear_plataforma(self._slave,False,False,False,(70,10),1130,200,r"mario-bros\Recursos\fondo.png")
            plataforma_diagonal_arriba_tres = crear_plataforma(self._slave,False,False,False,(70,10),1200,230,r"mario-bros\Recursos\fondo.png")
            plataformas= [piso,plataforma_invisible_2,plataforma_diagonal_abajo,plataforma_diagonal_abajo_dos,plataforma_diagonal_arriba,plataforma_diagonal_arriba_tres,plataforma_diagonal_arriba_dos ,plataforma_invisible,plataforma_invisible_3,plataforma_invisible_4]        
        if self.nivel == "nivel_tres":
            piso = crear_plataforma(self._slave,False,False,False, (630,20), 570, 470, r"spiderman_game\Recursos\fondos\fondo-1.jpg")
            plataforma_invisible = crear_plataforma(self._slave,False,False,False,(630,20),570,470,r"spiderman_game\Recursos\fondos\fondo-1.jpg")

            plataforma_invisible_2 = crear_plataforma(self._slave,False,False,False,(630,20),570,280,r"spiderman_game\Recursos\fondos\fondo-1.jpg")
            premio = crear_plataforma(self._slave,False,True,False,(60,50),1200,410,"")
            
            plataformas= [piso,plataforma_invisible_2,plataforma_invisible,premio]
        #ACTUALIZAR PERSONAJE
        if self.bandera_pausa == False:
            self.jugador.actualizar(self._slave, plataformas)
            
        
        #CREANDO OBJETOS
        self.primer_objeto.blitear_objeto(self._slave)
        self.segundo_objeto.blitear_objeto(self._slave)
        if self.jugador.rectangulo_principal.colliderect(self.primer_objeto.rectangulo_principal) and self.primer_objeto.agarrado == False:
            self.jugador.cant_telarañas = self.jugador.cant_telarañas + 10
            self.jugador.puntaje -= 100
            self.primer_objeto.agarrado = True
            
        if self.jugador.rectangulo_principal.colliderect(self.segundo_objeto.rectangulo_principal) and self.segundo_objeto.agarrado == False:
            self.jugador.vida = self.jugador.vida + 30
            self.segundo_objeto.agarrado = True
            self.jugador.puntaje -= 100
        if self.jugador.vida > 100 and self.tercer_objeto.agarrado != True:
            self.jugador.vida = 100
        if self.jugador.cant_telarañas > 50 and self.tercer_objeto.agarrado != True:
            self.jugador.cant_telarañas = 50
        if self.jugador.puntaje < 0:
            self.jugador.puntaje =0
        
        
        
        if self.nivel == "nivel_dos":
            if self.bandera_aparece_jefe == True and self.bandera_pausa == False:
                self.jefe.actualizar(self._slave)
                if tiempo_actual -self.tiempo_ultimo_disparo >= 500  and self.jefe.vida !=0 and self.bandera_pausa == False:
                    self.jefe.lanzar_simbionte()
                    self.tiempo_ultimo_disparo = tiempo_actual
                    
            self.jefe.colision_simbionte(self.jugador,self._slave)
            if self.jefe.vida ==0:
                self.tercer_objeto.blitear_objeto(self._slave)
                if self.jugador.rectangulo_principal.colliderect(self.tercer_objeto.rectangulo_principal) and self.tercer_objeto.agarrado == False:
                    self.jugador = Personaje(self.diccionario_black,(70,60),self.tercer_objeto.rectangulo_principal.x,self.tercer_objeto.rectangulo_principal.y,20,200,100,self.jugador.puntaje,self._slave)
                    reescalar_imagenes(self.diccionario_black, 100,90)
                    self.tercer_objeto.agarrado = True
                    self.jugador.vida = 200
                    self.jugador.cant_telarañas = 100
        
        if self.tercer_objeto.agarrado == True:
            
            icono_spiderman = py.image.load(r"spiderman_game\Recursos\spider-man-black\logo.png")
            icono_spiderman = py.transform.scale(icono_spiderman,(70,70))
            self._slave.blit(icono_spiderman,(20,30))
            texto_spiderman = fuente.render(str(self.jugador.vida),False,self.color_cinco,self.color_seis)
            self._slave.blit(texto_spiderman,(100,30))
            texto_cant_telarañas = fuente.render(str(self.jugador.cant_telarañas),False,self.color_cinco,self.color_seis)
            icono_cant_telarañas = py.image.load(r"spiderman_game\Recursos\spider-man\telaraña.png")
            icono_cant_telarañas =  py.transform.scale(icono_cant_telarañas,(70,70))
            self._slave.blit(icono_cant_telarañas,(20,90))
            self._slave.blit(texto_cant_telarañas,(100,105))
            icono_cant_puntaje = py.image.load(r"spiderman_game\Recursos\spider-man-black\score-black.png")
            icono_cant_puntaje =  py.transform.scale(icono_cant_puntaje,(70,40))
            self._slave.blit(icono_cant_puntaje,(20,150))
            puntaje = fuente.render(str(self.jugador.puntaje),True,self.color_cinco,self.color_seis)
            self._slave.blit(puntaje,(100,150))
        
        if self.nivel == "nivel_tres":
            if self.jefe.vida <= 0 and self.jefe_esta_muerto== False:
                self.jugador.puntaje += 1000
                self.jefe_esta_muerto = True
            if self.jefe_dos.vida <= 0 and self.greengoblin_esta_muerto== False:
                self.jugador.puntaje += 1000
                self.greengoblin_esta_muerto = True
            
            if self.villano_uno.vida <= 0 and self.villano_dos.vida <=0:
                self.bandera_aparece_jefe = True
                self.bandera_aparece_greengoblin = True
            
            if self.bandera_aparece_jefe == True and self.bandera_aparece_greengoblin == True and self.bandera_pausa == False:
                self.jefe.actualizar(self._slave)
                self.jefe_dos.actualizar_greengoblin(self._slave)
                if tiempo_actual - self.tiempo_ultimo_disparo_greengoblin >= 300 and self.jefe_dos.vida !=0 and self.bandera_pausa == False:
                    
                    self.jefe_dos.greengoblin_lanza_granada()
                    self.tiempo_ultimo_disparo_greengoblin = tiempo_actual
                if tiempo_actual - self.tiempo_ultimo_disparo >= 300 and self.jefe.vida !=0 and self.bandera_pausa == False:
                    self.jefe.hobgoblin_lanza_granada()
                    
                    self.tiempo_ultimo_disparo = tiempo_actual
            if self.villano_uno.vida <= 0 and self.villano_dos.vida <=0 and self.bandera_aparece_jefe == True and self.bandera_aparece_greengoblin == True:
                texto_hobgoblin = fuente.render(str(self.jefe.vida),False,self.color_uno,self.color_siete)
                icono_hobgoblin = py.image.load(r"spiderman_game\Recursos\hob-goblin\logo.png")
                icono_hobgoblin = py.transform.scale(icono_hobgoblin,(70,70))
                self._slave.blit(icono_hobgoblin,(960,20))
                self._slave.blit(texto_hobgoblin,(910,30))
                texto_greengoblin = fuente.render(str(self.jefe_dos.vida),False,self.color_cuatro,self.color_tres)
                icono_greengoblin = py.image.load(r"spiderman_game\Recursos\green-goblin\logo.png")
                icono_greengoblin = py.transform.scale(icono_greengoblin,(70,70))
                self._slave.blit(icono_greengoblin,(1100,20))
                self._slave.blit(texto_greengoblin,(1050,30))
            if self.bandera_pausa == False:
                self.jefe.colision_simbionte(self.jugador,self._slave)
                self.jefe_dos.colision_simbionte(self.jugador,self._slave)
        #DERROTA VIDA
        if self.jugador.vida == 0:
            cartel_game_over = py.image.load(r"spiderman_game\Recursos\fondos\fondo-game-over.png")
            cartel_game_over = py.transform.scale(cartel_game_over,(1220,720))
            self._slave.blit(cartel_game_over,(0,-35))
            puntaje = fuente.render(str(self.jugador.puntaje),True,self.color_uno,self.color_dos)
            self._slave.blit(puntaje,(1050,250))
        
        #DERROTA TIEMPO
        if self.tiempo<=0 and self.jefe.vida !=0 :
            cartel_game_over = py.image.load(r"spiderman_game\Recursos\fondos\fondo-game-over.png")
            cartel_game_over = py.transform.scale(cartel_game_over,(1220,720))
            self._slave.blit(cartel_game_over,(0,-35))
            puntaje = fuente.render(str(self.jugador.puntaje),True,self.color_uno,self.color_dos)
            self._slave.blit(puntaje,(1050,250))
            supero_tiempo = fuente.render("Superaste el limite",True,self.color_uno,self.color_dos)
            supero_tiempo_dos = fuente.render("de tiempo.",True,self.color_uno,self.color_dos)
            self._slave.blit(supero_tiempo,(950,500))
            self._slave.blit(supero_tiempo_dos,(990,539))

        #PUNTOS NIVEL
        if self.nivel == "nivel_uno" and self.jefe.vida <=0:
            cartel_final = py.image.load(r"spiderman_game\GUI\Recursos\nivel_completado.png")
            cartel_final = py.transform.scale(cartel_final,(400,120))
            self._slave.blit(cartel_final,(400,100))
            self.tiempo + 1
            if self.tiempo >= 30 and self.bandera_ya_sumo_tiempo_uno == False:
                self.jugador.puntaje = self.jugador.puntaje + 50000
                self.bandera_ya_sumo_tiempo_uno = True
        if self.nivel == "nivel_dos" and self.jefe.vida <=0:
            cartel_final = py.image.load(r"spiderman_game\GUI\Recursos\nivel_completado.png")
            cartel_final = py.transform.scale(cartel_final,(400,120))
            self._slave.blit(cartel_final,(400,100))
            self.tiempo +1
            if self.tiempo >= 30 and self.bandera_ya_sumo_tiempo_dos == False:
                self.jugador.puntaje = self.jugador.puntaje + 1000
                self.bandera_ya_sumo_tiempo_dos = True

        if self.nivel == "nivel_tres" and self.jefe.vida <= 0 and self.jefe_dos.vida <=0:
            cartel_final = py.image.load(r"spiderman_game\GUI\Recursos\termino_juego.png")
            cartel_final = py.transform.scale(cartel_final,(1200,680))
            self._slave.blit(cartel_final,(0,0))
            puntajes= lectura_partida_json()
            puntaje_final_numero = puntajes["puntaje_nivel_tres"]
            puntaje_final_numero = fuente.render(str(puntaje_final_numero),True,self.color_uno,self.color_dos)
            puntaje_final_texto = fuente.render("PUNTAJE FINAL:",True,self.color_uno,self.color_dos)

            self._slave.blit(puntaje_final_numero,(700,600))
            self._slave.blit(puntaje_final_texto,(500,600))
            self.tiempo + 1
            if self.tiempo >= 30 and self.bandera_ya_sumo_tiempo_tres == False:
                self.jugador.puntaje = self.jugador.puntaje + 1500
                self.bandera_ya_sumo_tiempo_tres = True
        
        #ARCHIVOS
        
        if self.jefe.vida ==0  and self.nivel == "nivel_uno" and self.bandera_juego_iniciado ==True:
            escribir_partida_json(True,False,False,self.jugador.puntaje,self.jugador.puntaje,self.jugador.puntaje)
            self.bandera_juego_iniciado =False
        if self.jefe.vida ==0 and self.villano_dos.vida ==0 and self.villano_uno.vida ==0 and self.nivel == "nivel_dos" and self.bandera_juego_iniciado_dos ==True :
            escribir_partida_json(True,True,False,self.jugador.puntaje,self.jugador.puntaje,self.jugador.puntaje)
            self.bandera_juego_iniciado_dos =False
        if self.nivel == "nivel_tres"and self.jefe.vida ==0 and  self.jefe_dos.vida == 0 and self.bandera_juego_iniciado_tres == True:
            escribir_partida_json(True,True,True,self.jugador.puntaje,self.jugador.puntaje,self.jugador.puntaje)
            nombres = lectura_nombre_json()
            with sqlite3.connect(r"spiderman_game\archivos\base_de_datos.db") as conexion:
                try:
                    sentencia= '''
                    insert into ranking(jugador,puntaje) values(?,?)
                    '''
                    conexion.execute(sentencia,(nombres["Nombre_usuario"],self.jugador.puntaje))
                except KeyError:
                    print("NO EXISTE LA CLAVE")
            
            self.bandera_juego_iniciado_tres =False

        
        if obtener_modo():
            py.draw.rect(self._slave, "blue", self.jugador.rectangulo_principal,3)
            py.draw.rect(self._slave, "blue", self.primer_objeto.rectangulo_principal,3)
            py.draw.rect(self._slave, "blue", self.segundo_objeto.rectangulo_principal,3)
            py.draw.rect(self._slave, "blue", self.jefe.rectangulo_principal,3)
            py.draw.rect(self._slave, "red", self.jugador.rectangulo_principal_derecha,3)
            py.draw.rect(self._slave, "red", self.jugador.rectangulo_principal_abajo,3)
            py.draw.rect(self._slave, "red", self.jugador.rectangulo_principal_izquierda,3)
            py.draw.rect(self._slave, "red", self.jugador.rectangulo_principal_izquierda_golpe,3)
            py.draw.rect(self._slave, "red", self.jugador.rectangulo_principal_derecha_golpe,3)
            py.draw.rect(self._slave, "blue", self.villano_uno.rectangulo_principal,3)
            py.draw.rect(self._slave, "blue", self.villano_dos.rectangulo_principal,3)
            for plataforma in plataformas:
                py.draw.rect(self._slave, "red", plataforma["rectangulo"], 3)
            
    
    
    
    def actualizar_pantalla(self):
        self._slave.blit(self.img_fondo,(0,0))
        for plataforma in self.plataformas:
            plataforma.draw(self._slave)
        self.jugador.update(self._slave,self.plataformas)

    def leer_inputs(self):
        teclas = py.key.get_pressed()

        if teclas[py.K_RIGHT] and self.jugador.animacion_actual != self.jugador.animaciones["derrotado"]:
            self.jugador.que_hace = "Derecha"
            bandera_disparo = True
            self.jugador.ultimo_movimiento = "Derecha"
        elif teclas[py.K_LEFT] and self.jugador.animacion_actual != self.jugador.animaciones["derrotado"]:
            self.jugador.que_hace = "Izquierda"
            bandera_disparo = True
            self.jugador.ultimo_movimiento = "Izquierda"
        elif(teclas[py.K_SPACE]) and self.jugador.animacion_actual != self.jugador.animaciones["derrotado"]:
            self.jugador.que_hace = "Salta"
            bandera_disparo = True
        elif self.jugador.animacion_actual != self.jugador.animaciones["derrotado"]:
            if self.jugador.ultimo_movimiento == "Derecha":
                self.jugador.que_hace = "Quieto"
            if self.jugador.ultimo_movimiento == "Izquierda":
                self.jugador.que_hace = "Quieto_izquierda"
        bandera_disparo = True

    def dibujar_rectangulos(self):
        if obtener_modo():
            py.draw.rect(self._slave, "blue", self.jugador.rectangulo_principal,3)
            py.draw.rect(self._slave, "red", self.jugador.rectangulo_principal,3)
            py.draw.rect(self._slave, "blue", self.jugador.rectangulo_principal,3)
            #py.draw.rect(self._slave, "blue", self.jugador.rectangulo_abajo,3)
            #for plataforma in self.plataformas:
            #    py.draw.rect(self._slave, "red", plataforma["rectangulo"], 3)
        