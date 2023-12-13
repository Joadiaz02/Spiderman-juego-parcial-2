import pygame
import sys
from pygame.locals import *
from GUI.UI.GUI_form_prueba import FormPrueba
from GUI.UI.GUI_form import Form

pygame.init()
WIDTH = 1200
HEIGHT = 600
FPS = 60

reloj = pygame.time.Clock()
pantalla = pygame.display.set_mode((WIDTH, HEIGHT))

form_prueba = FormPrueba(pantalla,0,0,1200,600,"red","blue",5,True)#el ultimo parametro dice si se muestra o no.

while True:
    reloj.tick(FPS)
    eventos = pygame.event.get()
    for event in eventos:
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pantalla.fill("Black")
    form_prueba.update(eventos)
    
    pygame.display.flip()