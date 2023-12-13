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
from Class_nivel_uno import NivelUno 
from Class_nivel_dos import NivelDos
from Class_nivel_tres import NivelTres
from archivos.funciones import *
from GUI.UI.GUI_form_prueba import *
import re
import sqlite3


#py.init()
RELOJ = py.time.Clock()
FPS = 18
WIDTH = 1200
HEIGHT = 680
W,H = 1200, 680
PANTALLA = py.display.set_mode((WIDTH,HEIGHT)) # En pixeles
flag = True
#fuente = py.font.SysFont("Arial",30)
#pantalla_menu = py.display.set_mode((WIDTH, HEIGHT))

#nivel_actual = NivelTres(PANTALLA)
nombre_jugador = ""
form_principal = FormPrueba(PANTALLA,0,0,1200,680,"red","blue",5,True)#el ultimo parametro dice si se muestra o no.
inicio_juego = False
while flag:
    RELOJ.tick(FPS)
    nombres=lectura_nombre_json()
    if nombres["Nombre_usuario"] == "":
        try:
            
            nombre_jugador=input("Ingrese su nombre: ")
            nombre_jugador = str(nombre_jugador)
            nombre_jugador_dos = re.sub("[?¡¿!}{$@]+","",str(nombre_jugador))
            nombre_jugador_tres = re.sub(" ","",nombre_jugador_dos)#remplazamos los espacios por un (.)
            escribir_nombre_json(nombre_jugador_tres)
            inicio_juego= True
        except SyntaxError:
            print("ERROR DE SINTAXIS")
    
    
    
    eventos = py.event.get()
    for event in eventos:
        if event.type == QUIT:
            flag = False
        
    
    form_principal.update(eventos)
    
        
    
    
    
    
    
    

    py.display.update()

py.quit()