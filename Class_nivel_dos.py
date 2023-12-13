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
class NivelDos(Nivel):
    def __init__(self,PANTALLA):
        #W,H = 1200, 680
        FPS = 18 #Para desacelerar la pantalla
        ROJO = (255,0,0)
        AZUL = (0,0,255)
        VIOLETA =(120,40,140)
        VERDE=(100,255,0)
        BLANCO = (255,255,255)
        NEGRO = (0,0,0)
        W = PANTALLA.get_width()
        H = PANTALLA.get_height()
        RELOJ = py.time.Clock()
        #PANTALLA = py.display.set_mode((W,H)) # En pixeles
        py.display.set_caption("Spiderman the video game (2023)")
        fuente = py.font.SysFont("Arial",30)
        #FONDO
        fondo = py.image.load(r"spiderman_game\Recursos\fondos\fondo-2.jfif").convert()#acelera el juego y hace que consuma menos recursos
        fondo = py.transform.scale(fondo, (W,H))


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
        diccionario_recibido = diccionario
        spiderman = Personaje(diccionario_recibido,(70,60),600,350,20,100,50,0,PANTALLA)
        reescalar_imagenes(diccionario, 100,90)
        reescalar_imagenes(diccionario_black, 100,90)
        

        
        

        #Topes
        primera_tope_izquierda = crear_plataforma(PANTALLA,False,False,False,(10,40),50,265,r"mario-bros\Recursos\fondo.png")
        primera_tope_derecha = crear_plataforma(PANTALLA,False,False,False,(10,40),350,265,r"mario-bros\Recursos\fondo.png")
        segundo_tope_izquierda = crear_plataforma(PANTALLA,False,False,False,(10,40),530,275,r"mario-bros\Recursos\fondo.png")
        segundo_tope_derecha = crear_plataforma(PANTALLA,False,False,False,(10,40),815,275,r"mario-bros\Recursos\fondo.png")
        tercer_tope_izquierda = crear_plataforma(PANTALLA,False,False,False,(10,40),0,410,r"mario-bros\Recursos\fondo.png")
        tercer_tope_derecha = crear_plataforma(PANTALLA,False,False,False,(10,40),750,410,r"mario-bros\Recursos\fondo.png")

        #plataforma_movil_nivel_uno = crear_plataforma_movil(True,False,True,(100,20),50,eje_y,r"spiderman_game\Recursos\fondos\planeador.png")

        #plataformas= [piso,plataforma_invisible_2,plataforma_diagonal_abajo,plataforma_diagonal_arriba,plataforma_diagonal_arriba_tres,plataforma_diagonal_arriba_dos ,plataforma_invisible,premio,plataforma_invisible_3,plataforma_invisible_4]





        #ENEMIGOS

        diccionario_animaciones_venom = {"izquierda": venom_camina_izquierda, "derrotado": venom_derrotado_1, "quieto": venom_quieto, "derecha":venom_camina_derecha}
        diccionario_animaciones_scorpion = {"izquierda": scorpion_camina_izquierda, "derecha": scorpion_camina_derecha, "derrotado": scorpion_derrotado}
        diccionario_animaciones_scorpion_dos = {"izquierda": scorpion_camina_izquierda, "derecha": scorpion_camina_derecha, "derrotado": scorpion_derrotado}
        #diccionario_animaciones_electro = {"disparo": electro_disparo, "derrotado":electro_derrotado,"quieto":electro_quieto,"dispara":electro_dispara}

        scorpion = Enemigo(diccionario_animaciones_scorpion,530,190,"izquierda",segundo_tope_izquierda,segundo_tope_derecha,10,240,PANTALLA)
        scorpion_dos = Enemigo(diccionario_animaciones_scorpion_dos,200,190,"izquierda",primera_tope_izquierda,primera_tope_derecha,10,240,PANTALLA)
        #electro = Enemigo(diccionario_animaciones_electro,850,200,"quieto")

        derrotado_venom = {"derrotado": diccionario_animaciones_venom["derrotado"]}
        derrotado_scorpion = {"derrotado": diccionario_animaciones_scorpion["derrotado"]}
        reescalar_imagenes(derrotado_venom,100,80)
        reescalar_imagenes(derrotado_scorpion,80,60)

        #global bandera_aparece_Venom
        bandera_aparece_venom = False


        venom = Enemigo(diccionario_animaciones_venom,-100,390,"derecha",tercer_tope_izquierda,tercer_tope_derecha,100,390,PANTALLA)        
        lista_enemigos = [venom,scorpion, scorpion_dos]

        scorpion_esta_muerto = False
        scorpion_dos_esta_muerto = False
        venom_esta_muerto = False

        #OBJETOS
        diccionario_objetos = {"cartucho": recarga_telaraña, "corazon": incremento_vida,"simbionte": bola_simbionte}

        primer_objeto = Objeto(diccionario_objetos,"cartucho",1010,200)
        segundo_objeto = Objeto(diccionario_objetos,"corazon",1120,440)
        tercer_objeto = Objeto(diccionario_objetos,"simbionte",450,400)

        bandera_disparo= False
        tiempo_ultimo_disparo = 0
        que_hace = "Quieto"
        aux = 1
        tiempo = py.time.get_ticks()/1000
        bandera_pausa = False

        flag = True

        super().__init__(PANTALLA,"nivel_dos",spiderman,venom,scorpion,scorpion_dos,fondo,AZUL,ROJO,VIOLETA,VERDE,BLANCO,NEGRO,AZUL,VIOLETA,primer_objeto,segundo_objeto,tercer_objeto,scorpion_esta_muerto,scorpion_dos_esta_muerto,venom_esta_muerto,bandera_aparece_venom,bandera_disparo,tiempo_ultimo_disparo,que_hace,aux,flag,fuente,eje_y,diccionario_black,lista_enemigos,bandera_pausa,tiempo)