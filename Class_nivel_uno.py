import pygame as py
from pygame.locals import *
from Configuraciones import *
from os import system
system("cls")
from Class_Personaje import Personaje
from Modo import *
from Class_enemigo import Enemigo
from Class_objeto import Objeto
import time 
from nivel import Nivel
from funcion_plataforma import * 
#from main import nombre_jugador
class NivelUno(Nivel):
    def __init__(self,PANTALLA: py.Surface):
        
        ROJO = (255,0,0)
        AZUL = (0,0,255)
        VIOLETA =(120,40,140)
        VERDE=(100,255,0)
        #eje_y = 500
        
        
        W = PANTALLA.get_width()
        H = PANTALLA.get_height()
        #ANCHO W - ALTO H
        
        FPS = 18 #Para desacelerar la pantalla

        
        py.display.set_caption("Spiderman the video game (2023)")
        fuente = py.font.SysFont("Arial",30)
        #FONDO
        fondo = py.image.load(r"spiderman_game\Recursos\fondos\fondo-1.jpg").convert()#acelera el juego y hace que consuma menos recursos
        fondo = py.transform.scale(fondo, (W,H))

        #SPIDER-MAN

        diccionario = {}
        diccionario["Quieto"] = personaje_quieto
        diccionario["Quieto_izquierda"] = personaje_quieto_izquierda
        diccionario["Derecha"] = personaje_camina_derecha
        diccionario["Izquierda"] = personaje_camina_izquierda
        diccionario["Salta"] = personaje_salta
        diccionario["cae"] = personaje_cae
        diccionario["derrotado"] = personaje_derrotado
        diccionario["super_derecha"] = spiderblack_derecha
        diccionario["super_izquierda"] = spiderblack_izquierda
        diccionario["super_quieto"] = spiderblack_quieto
        diccionario["super_salta"] = spiderblack_salta
        diccionario["dispara_izquierda"] = personaje_dispara_izquierda
        diccionario["dispara_derecha"] = personaje_dispara_derecha
        diccionario["golpea_derecha"] = personaje_golpea_derecha
        diccionario["golpea_izquierda"] = personaje_golpea_izquierda

        spiderman = Personaje(diccionario,(70,60),600,500,20,100,50,0,PANTALLA)
        reescalar_imagenes(diccionario, 100,90)

        #OBJETOS
        diccionario_objetos = {"cartucho": recarga_telaraña, "corazon": incremento_vida,"simbionte": bola_simbionte}

        primer_objeto = Objeto(diccionario_objetos,"cartucho",719,180)
        segundo_objeto = Objeto(diccionario_objetos,"corazon",1120,370)
        tercer_objeto = Objeto(diccionario_objetos,"simbionte",1120,370)
        #PLATAFORMAS
        
        #Topes
        primera_tope_izquierda = crear_plataforma(PANTALLA,False,False,False,(10,40),215,580,r"mario-bros\Recursos\fondo.png")
        primera_tope_derecha = crear_plataforma(PANTALLA,False,False,False,(10,40),1190,580,r"mario-bros\Recursos\fondo.png")
        segundo_tope_izquierda = crear_plataforma(PANTALLA,False,False,False,(10,40),200,180,r"mario-bros\Recursos\fondo.png")
        segundo_tope_derecha = crear_plataforma(PANTALLA,False,False,False,(10,40),750,180,r"mario-bros\Recursos\fondo.png")
        tercer_tope_izquierda = crear_plataforma(PANTALLA,False,False,False,(10,40),200,350,r"mario-bros\Recursos\fondo.png")
        tercer_tope_derecha = crear_plataforma(PANTALLA,False,False,False,(10,40),750,350,r"mario-bros\Recursos\fondo.png")

        




        #ENEMIGOS
        diccionario_animaciones_lizard = {"izquierda": enemigo_camina, "derrotado": enemigo_derrotado_1, "quieto": enemigo_quieto, "derecha":enemigo_camina_derecha}
        diccionario_animaciones_scorpion = {"izquierda": scorpion_camina_izquierda, "derecha": scorpion_camina_derecha, "derrotado": scorpion_derrotado}
        diccionario_animaciones_scorpion_dos = {"izquierda": scorpion_camina_izquierda, "derecha": scorpion_camina_derecha, "derrotado": scorpion_derrotado}

        scorpion = Enemigo(diccionario_animaciones_scorpion,650,150,"izquierda",segundo_tope_izquierda,segundo_tope_derecha,10,200,PANTALLA)
        scorpion_dos = Enemigo(diccionario_animaciones_scorpion_dos,650,350,"izquierda",tercer_tope_izquierda,tercer_tope_derecha,10,390,PANTALLA)
        lizard = Enemigo(diccionario_animaciones_lizard,1200,535,"izquierda",primera_tope_izquierda,primera_tope_derecha,100,550,PANTALLA)        

        derrotado_lizard = {"derrotado": diccionario_animaciones_lizard["derrotado"]}
        derrotado_scorpion = {"derrotado": diccionario_animaciones_scorpion["derrotado"]}
        reescalar_imagenes(derrotado_lizard,100,80)
        reescalar_imagenes(derrotado_scorpion,80,60)

        #lista_enemigos = [lizard,scorpion, scorpion_dos]

        scorpion_esta_muerto = False
        scorpion_dos_esta_muerto = False
        lizard_esta_muerto = False
        bandera_aparece_lizard = False

        lista_enemigos = [scorpion,scorpion_dos,lizard]

        #Personaje
        x_inicial = W//2 - 400
        y_inicial = 560
        rectangulo_personaje = personaje_quieto[0].get_rect()
        rectangulo_personaje.x = x_inicial
        rectangulo_personaje.y = y_inicial
        bandera_disparo= False
        tiempo_ultimo_disparo = 0
        que_hace = "Quieto"
        
        #TIEMPO
        tiempo = 1
        
        aux = 1
        

        bandera_pausa = False

        flag = True
        
        super().__init__(PANTALLA,"nivel_uno",spiderman,lizard,scorpion,scorpion_dos,fondo,AZUL,ROJO,VIOLETA,VERDE,VERDE,ROJO,AZUL,VIOLETA,primer_objeto,segundo_objeto,tercer_objeto,scorpion_esta_muerto,scorpion_dos_esta_muerto,lizard_esta_muerto,bandera_aparece_lizard,bandera_disparo,tiempo_ultimo_disparo,que_hace,aux,flag,fuente,eje_y,diccionario,lista_enemigos,bandera_pausa,tiempo)