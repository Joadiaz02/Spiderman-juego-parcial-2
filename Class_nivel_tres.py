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
class NivelTres(Nivel):
    def __init__(self,PANTALLA):
        ROJO = (255,0,0)
        AZUL = (0,0,255)
        VIOLETA =(120,40,140)
        VERDE=(100,255,0)
        BLANCO = (255,255,255)
        NEGRO = (0,0,0)
        NARANJA = (255,128,0)
        #W,H = 1200, 680
        FPS = 18 #Para desacelerar la pantalla
        W = PANTALLA.get_width()
        H = PANTALLA.get_height()
        py.init()
        RELOJ = py.time.Clock()
        #PANTALLA = py.display.set_mode((W,H)) # En pixeles
        py.display.set_caption("Spiderman the video game (2023)")
        fuente = py.font.SysFont("Arial",30)
        #FONDO
        fondo = py.image.load(r"spiderman_game\Recursos\fondos\fondo-3.jpg").convert()#acelera el juego y hace que consuma menos recursos
        fondo = py.transform.scale(fondo, (W,H))



        contador_pasos = 0

        diccionario = {}
        diccionario_black ={}
        diccionario["Quieto"] = personaje_quieto
        diccionario["Quieto_izquierda"] = personaje_quieto_izquierda
        diccionario["Derecha"] = personaje_camina_derecha
        diccionario["Izquierda"] = personaje_camina_izquierda
        diccionario["Salta"] = personaje_salta
        diccionario["cae"] = personaje_cae
        diccionario["derrotado"] = personaje_derrotado
        diccionario["golpea_derecha"] = personaje_golpea_derecha
        diccionario["golpea_izquierda"] = personaje_golpea_izquierda


        diccionario_black["Derecha"] = spiderblack_derecha
        diccionario_black["Izquierda"] = spiderblack_izquierda
        diccionario_black["Quieto_izquierda"] = spiderblack_quieto_izquierda
        diccionario_black["Quieto"] = spiderblack_quieto
        diccionario_black["Salta"] = spiderblack_salta
        diccionario_black["derrotado"] = spiderblack_derrotado
        diccionario_black["dispara_izquierda"] = personaje_dispara_izquierda
        diccionario_black["dispara_derecha"] = personaje_dispara_derecha
        diccionario_black["cae"] = personaje_cae
        diccionario_black["golpea_derecha"] = spiderblack_golpea_derecha
        diccionario_black["golpea_izquierda"] = spiderblack_golpea_izquierda


        diccionario["dispara_izquierda"] = personaje_dispara_izquierda
        diccionario["dispara_derecha"] = personaje_dispara_derecha
        #diccionario_recibido = diccionario
        spiderman = Personaje(diccionario_black,(70,60),1100,350,20,200,100,0,PANTALLA)
        reescalar_imagenes(diccionario, 100,90)
        reescalar_imagenes(diccionario_black, 100,90)

        #OBJETOS
        diccionario_objetos = {"cartucho": recarga_telaraña, "corazon": incremento_vida,"simbionte": bola_simbionte}

        primer_objeto = Objeto(diccionario_objetos,"cartucho",1010,200)
        segundo_objeto = Objeto(diccionario_objetos,"corazon",620,440)
        tercer_objeto = Objeto(diccionario_objetos,"simbionte",320,400)
        tercer_objeto.agarrado = True
        #PLATAFORMAS
        

        #Topes
        primera_tope_izquierda = crear_plataforma(PANTALLA,False,False,False,(10,40),650,465,r"mario-bros\Recursos\fondo.png")
        primera_tope_derecha = crear_plataforma(PANTALLA,False,False,False,(10,40),1050,465,r"mario-bros\Recursos\fondo.png")
        segundo_tope_izquierda = crear_plataforma(PANTALLA,False,False,False,(10,40),530,275,r"mario-bros\Recursos\fondo.png")
        segundo_tope_derecha = crear_plataforma(PANTALLA,False,False,False,(10,40),815,275,r"mario-bros\Recursos\fondo.png")
        tercer_tope_izquierda = crear_plataforma(PANTALLA,False,False,False,(10,40),585,110,r"mario-bros\Recursos\fondo.png")
        tercer_tope_derecha = crear_plataforma(PANTALLA,False,False,False,(10,40),1200,110,r"mario-bros\Recursos\fondo.png")
        cuarto_tope_arriba = crear_plataforma(PANTALLA,False,False,False,(100,40),405,50,r"mario-bros\Recursos\fondo.png")
        cuarto_tope_abajo = crear_plataforma(PANTALLA,False,False,False,(100,40),405,540,r"mario-bros\Recursos\fondo.png")
        

        

        #SIMBIONTE
        simbionte={}
        #obtenemos_imagen
        simbionte["superficie"] = bola_simbionte[0]
        simbionte["superficie"] = py.transform.scale(simbionte["superficie"],(60,70))
        #rectangulo_dibujo
        simbionte["rectangulo"] = simbionte["superficie"].get_rect()
        #ubicacion
        simbionte["rectangulo"].x = 300
        simbionte["rectangulo"].x = 400

        #UPGRADE DE VIDA
        upgrade_vida={}
        #obtenemos_imagen
        upgrade_vida["superficie"] = bola_simbionte[0]
        upgrade_vida["superficie"] = py.transform.scale(upgrade_vida["superficie"],(60,70))
        #rectangulo_dibujo
        upgrade_vida["rectangulo"] = upgrade_vida["superficie"].get_rect()
        upgrade_vida["rectangulo"].x = 1100
        upgrade_vida["rectangulo"].y = 423
        PANTALLA.blit(upgrade_vida["superficie"],(589, 359) )
        #ubicacion



        #ENEMIGOS

        diccionario_animaciones_hobgoblin = {"izquierda": hobgoblin_camina_izquierda, "derrotado": hobgoblin_derrotado,  "derecha":hobgoblin_camina_derecha}
        diccionario_animaciones_greengoblin = {"sube": greengoblin_mueve, "derrotado": greengoblin_derrotado}
        diccionario_animaciones_scorpion = {"izquierda": scorpion_camina_izquierda, "derecha": scorpion_camina_derecha, "derrotado": scorpion_derrotado}
        diccionario_animaciones_scorpion_dos = {"izquierda": scorpion_camina_izquierda, "derecha": scorpion_camina_derecha, "derrotado": scorpion_derrotado}
        #diccionario_animaciones_electro = {"disparo": electro_disparo, "derrotado":electro_derrotado,"quieto":electro_quieto,"dispara":electro_dispara}

        scorpion = Enemigo(diccionario_animaciones_scorpion,530,190,"izquierda",segundo_tope_izquierda,segundo_tope_derecha,10,240,PANTALLA)
        scorpion_dos = Enemigo(diccionario_animaciones_scorpion_dos,700,400,"izquierda",primera_tope_izquierda,primera_tope_derecha,10,440,PANTALLA)
        #electro = Enemigo(diccionario_animaciones_electro,850,200,"quieto")

        derrotado_hobgoblin = {"derrotado": diccionario_animaciones_hobgoblin["derrotado"]}
        derrotado_greengoblin = {"derrotado": diccionario_animaciones_greengoblin["derrotado"]}
        derrotado_scorpion = {"derrotado": diccionario_animaciones_scorpion["derrotado"]}
        reescalar_imagenes(derrotado_hobgoblin,80,70)
        reescalar_imagenes(derrotado_greengoblin,60,50)
        reescalar_imagenes(derrotado_scorpion,80,60)

        #global bandera_aparece_Venom
        bandera_aparece_hobgoblin = False
        bandera_aparece_greengoblin = False

        hobgoblin = Enemigo(diccionario_animaciones_hobgoblin,1200,90,"izquierda",tercer_tope_izquierda,tercer_tope_derecha,100,230,PANTALLA)
        greengoblin = Enemigo(diccionario_animaciones_greengoblin,300,90,"sube",cuarto_tope_arriba,cuarto_tope_abajo,100,390,PANTALLA)        
        lista_enemigos = [hobgoblin,greengoblin,scorpion, scorpion_dos]

        scorpion_esta_muerto = False
        scorpion_dos_esta_muerto = False
        greengoblin_esta_muerto = False
        hobgoblin_esta_muerto = False

        #Personaje
        x_inicial = W//2 - 400
        y_inicial = 560
        rectangulo_personaje = personaje_quieto[0].get_rect()
        rectangulo_personaje.x = x_inicial
        rectangulo_personaje.y = y_inicial
        bandera_disparo= False
        tiempo_ultimo_disparo = 0
        tiempo_ultimo_disparo_greengoblin =0

        que_hace = "Quieto"
        aux = 1
        tiempo = py.time.get_ticks()/1000
        bandera_pausa = False

        flag = True
        super().__init__(PANTALLA,"nivel_tres",spiderman,hobgoblin,scorpion,scorpion_dos,fondo,AZUL,ROJO,VIOLETA,VERDE,BLANCO,NEGRO,NARANJA,VIOLETA,primer_objeto,segundo_objeto,tercer_objeto,scorpion_esta_muerto,scorpion_dos_esta_muerto,hobgoblin_esta_muerto,bandera_aparece_hobgoblin,bandera_disparo,tiempo_ultimo_disparo,que_hace,aux,flag,fuente,eje_y,diccionario_black,lista_enemigos,bandera_pausa,tiempo,greengoblin,bandera_aparece_greengoblin,greengoblin_esta_muerto,tiempo_ultimo_disparo_greengoblin)