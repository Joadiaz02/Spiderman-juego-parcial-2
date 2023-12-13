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

ROJO = (255,0,0)
AZUL = (0,0,255)
VIOLETA =(120,40,140)
VERDE=(100,255,0)
#eje_y = 500
def crear_plataforma(visible,esPremio,esMovil, tamaño,  x,  y:int,path=""):
    plataforma = {}
    eje_y = y
    movimiento_sube = True
    if visible and esMovil == False:
        plataforma["superficie"] = py.image.load(path)
        plataforma["superficie"] = py.transform.scale(plataforma["superficie"], tamaño)
        PANTALLA.blit(plataforma["superficie"],(x,eje_y))
        plataforma["rectangulo"] = plataforma["superficie"].get_rect()
        plataforma["rectangulo"].x = x
        plataforma["rectangulo"].y = y
    if visible and esMovil:
        if movimiento_sube == True:
            eje_y = eje_y - 10
            plataforma["superficie"] = py.image.load(path)
            plataforma["superficie"] = py.transform.scale(plataforma["superficie"], tamaño)
            PANTALLA.blit(plataforma["superficie"],(x,eje_y))
            plataforma["rectangulo"] = plataforma["superficie"].get_rect()
            plataforma["rectangulo"].x = x
            plataforma["rectangulo"].y = eje_y
        if eje_y < 200:
            movimiento_sube = False
        if movimiento_sube == False:
            eje_y=eje_y +120
            plataforma["superficie"] = py.image.load(path)
            plataforma["superficie"] = py.transform.scale(plataforma["superficie"], tamaño)
            PANTALLA.blit(plataforma["superficie"],(x,eje_y))
            plataforma["rectangulo"] = plataforma["superficie"].get_rect()
            plataforma["rectangulo"].x = x
            plataforma["rectangulo"].y = eje_y
        if eje_y > 600:
            movimiento_sube = True


    else:
        plataforma["superficie"] = py.Surface(tamaño)

    plataforma["rectangulo"] = plataforma["superficie"].get_rect()
    plataforma["rectangulo"].x = x
    plataforma["rectangulo"].y = y
    plataforma["premio"] = esPremio
    return plataforma

movimiento_sube = True
eje_y = 610
def crear_plataforma_movil(visible,esPremio,esMovil, tamaño,  x,  y:int,path=""):
    plataforma = {}
    global eje_y
    global movimiento_sube
    if visible and esMovil == False:
        plataforma["superficie"] = py.image.load(path)
        plataforma["superficie"] = py.transform.scale(plataforma["superficie"], tamaño)
        PANTALLA.blit(plataforma["superficie"],(x,eje_y))
        plataforma["rectangulo"] = plataforma["superficie"].get_rect()
        plataforma["rectangulo"].x = x
        plataforma["rectangulo"].y = y
    if visible and esMovil:
        
        #movimiento_sube = True
        if movimiento_sube == True:
            
            eje_y = eje_y - 10
            plataforma["superficie"] = py.image.load(path)
            plataforma["superficie"] = py.transform.scale(plataforma["superficie"], tamaño)
            
            plataforma["rectangulo"] = plataforma["superficie"].get_rect()
            plataforma["rectangulo"].x = x
            plataforma["rectangulo"].y = eje_y
            #plataforma["rectangulo"].y  -= 10
            PANTALLA.blit(plataforma["superficie"],(x,eje_y))
        if eje_y < 200:
            movimiento_sube = False
        if movimiento_sube == False:
            eje_y=eje_y +10
            plataforma["superficie"] = py.image.load(path)
            plataforma["superficie"] = py.transform.scale(plataforma["superficie"], tamaño)
            
            plataforma["rectangulo"] = plataforma["superficie"].get_rect()
            plataforma["rectangulo"].x = x
            plataforma["rectangulo"].y  = eje_y
            #plataforma["rectangulo"].y  += 10
            PANTALLA.blit(plataforma["superficie"],(x,eje_y))
            #PANTALLA.blit(plataforma["rectangulo"],(x,eje_y))
        if eje_y > 600:
            movimiento_sube = True
    else:
        plataforma["superficie"] = py.Surface(tamaño)
    plataforma["rectangulo"] = plataforma["superficie"].get_rect()
    plataforma["rectangulo"].x = x
    plataforma["rectangulo"].y = eje_y
    plataforma["premio"] = esPremio
    
    return plataforma

#ANCHO W - ALTO H
W,H = 1200, 680
FPS = 18 #Para desacelerar la pantalla

py.init()
RELOJ = py.time.Clock()
PANTALLA = py.display.set_mode((W,H)) # En pixeles
py.display.set_caption("Spiderman the video game (2023)")

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

spiderman = Personaje(diccionario,(70,60),600,500,20,100,50,0,PANTALLA)
reescalar_imagenes(diccionario, 100,90)

#OBJETOS
diccionario_objetos = {"cartucho": recarga_telaraña, "corazon": incremento_vida,"simbionte": bola_simbionte}

primer_objeto = Objeto(diccionario_objetos,"cartucho",719,180)
segundo_objeto = Objeto(diccionario_objetos,"corazon",1120,370)

#PLATAFORMAS
piso = crear_plataforma(True,False,False, (1200,20), 216, H-60, r"spiderman_game\Recursos\fondos\fondo-1.jpg")
plataforma_invisible= plataforma_invisible = crear_plataforma(True,False,False,(535,20),220,425,r"spiderman_game\Recursos\fondos\fondo-1.jpg")
plataforma_invisible_2 = crear_plataforma(True,False,False,(535,20),220,225,r"spiderman_game\Recursos\fondos\fondo-1.jpg")
premio = crear_plataforma(False,True,False,(60,50),1200,410,"")
plataforma_invisible_3 = crear_plataforma(False,False,False,(181,20),1014,425,r"mario-bros\Recursos\fondo.png")
plataforma_invisible_4 = crear_plataforma(False,False,False,(181,20),1014,225,r"mario-bros\Recursos\fondo.png")
zona_dispara_electro = crear_plataforma(False,False,False,(348,201),278,149,r"mario-bros\Recursos\fondo.png")

#Topes
primera_tope_izquierda = crear_plataforma(False,False,False,(10,40),215,580,r"mario-bros\Recursos\fondo.png")
primera_tope_derecha = crear_plataforma(False,False,False,(10,40),1190,580,r"mario-bros\Recursos\fondo.png")
segundo_tope_izquierda = crear_plataforma(False,False,False,(10,40),200,180,r"mario-bros\Recursos\fondo.png")
segundo_tope_derecha = crear_plataforma(False,False,False,(10,40),750,180,r"mario-bros\Recursos\fondo.png")
tercer_tope_izquierda = crear_plataforma(False,False,False,(10,40),200,350,r"mario-bros\Recursos\fondo.png")
tercer_tope_derecha = crear_plataforma(False,False,False,(10,40),750,350,r"mario-bros\Recursos\fondo.png")

#SIMBIONTE
simbionte={}
#obtenemos_imagen
simbionte["superficie"] = bola_simbionte[0]
simbionte["superficie"] = py.transform.scale(simbionte["superficie"],(60,70))
#rectangulo_dibujo
simbionte["rectangulo"] = simbionte["superficie"].get_rect()


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




#ENEMIGOS
diccionario_animaciones_lizard = {"izquierda": enemigo_camina, "derrotado": enemigo_derrotado_1, "quieto": enemigo_quieto, "derecha":enemigo_camina_derecha}
diccionario_animaciones_scorpion = {"izquierda": scorpion_camina_izquierda, "derecha": scorpion_camina_derecha, "derrotado": scorpion_derrotado}
diccionario_animaciones_scorpion_dos = {"izquierda": scorpion_camina_izquierda, "derecha": scorpion_camina_derecha, "derrotado": scorpion_derrotado}

scorpion = Enemigo(diccionario_animaciones_scorpion,650,150,"izquierda",segundo_tope_izquierda,segundo_tope_derecha,10,180,PANTALLA)
scorpion_dos = Enemigo(diccionario_animaciones_scorpion_dos,650,350,"izquierda",tercer_tope_izquierda,tercer_tope_derecha,10,390,PANTALLA)
lizard = Enemigo(diccionario_animaciones_lizard,1200,535,"izquierda",primera_tope_izquierda,primera_tope_derecha,100,550,PANTALLA)        

derrotado_lizard = {"derrotado": diccionario_animaciones_lizard["derrotado"]}
derrotado_scorpion = {"derrotado": diccionario_animaciones_scorpion["derrotado"]}
reescalar_imagenes(derrotado_lizard,100,80)
reescalar_imagenes(derrotado_scorpion,80,60)

lista_enemigos = [lizard,scorpion, scorpion_dos]

scorpion_esta_muerto = False
scorpion_dos_esta_muerto = False
lizard_esta_muerto = False
bandera_aparece_lizard = False

#Personaje
x_inicial = W//2 - 400
y_inicial = 560
rectangulo_personaje = personaje_quieto[0].get_rect()
rectangulo_personaje.x = x_inicial
rectangulo_personaje.y = y_inicial
bandera_disparo= False
tiempo_ultimo_disparo = 0
que_hace = "Quieto"
aux = 1

flag = True
while flag:
    RELOJ.tick(FPS)
    for event in py.event.get():
        if event.type == QUIT:
            flag = False
        elif event.type == MOUSEBUTTONDOWN:
            print(event.pos)
        

    
        
    
    fuente = py.font.SysFont("Arial",30)
    PANTALLA.blit(fondo,(0,0))

    #PLATAFORMA MOVIL, LISTA DE PLATAFORMAS Y TRAMPAS
    plataforma_movil_nivel_uno = crear_plataforma_movil(True,False,True,(100,50),50,eje_y,r"spiderman_game\Recursos\fondos\planeador.png")
    trampa = crear_plataforma(True,False,False,(120,50),1050,265,r"spiderman_game\Recursos\objetos\trampa.png")
    plataformas= [piso,plataforma_movil_nivel_uno, plataforma_invisible_2, plataforma_invisible,premio,plataforma_invisible_3,plataforma_invisible_4]
    if spiderman.rectangulo_principal.colliderect(trampa["rectangulo"]):
        spiderman.rectangulo_principal.y += 100
        spiderman.puntaje -= 50
        spiderman.vida = spiderman.vida -20
    
    #TIEMPO GAME OVER
    tiempo = py.time.get_ticks()/1000
    tiempo = int(tiempo)
    if aux == tiempo:
        aux +=1
    contador = fuente.render("Tiempo : "+str(tiempo),True,AZUL,ROJO)
    PANTALLA.blit(contador,(550,20))
    
    #VIDA SPIDER-MAN DISPLAY
    texto_spiderman = fuente.render(str(spiderman.vida),False,AZUL,ROJO)
    icono_spiderman = py.image.load(r"spiderman_game\Recursos\spider-man\vida-logo.png")
    icono_spiderman = py.transform.scale(icono_spiderman,(70,70))
    PANTALLA.blit(icono_spiderman,(20,30))
    PANTALLA.blit(texto_spiderman,(100,30))

    #CANTIDAD DE TELARAÑAS DISPLAY
    texto_cant_telarañas = fuente.render(str(spiderman.cant_telarañas),False,AZUL,ROJO)
    icono_cant_telarañas = py.image.load(r"spiderman_game\Recursos\spider-man\telaraña.png")
    icono_cant_telarañas =  py.transform.scale(icono_cant_telarañas,(70,70))
    PANTALLA.blit(icono_cant_telarañas,(20,90))
    PANTALLA.blit(texto_cant_telarañas,(100,105))
    
    #PUNTAJE DISPLAY
    icono_cant_puntaje = py.image.load(r"spiderman_game\Recursos\fondos\score.png")
    icono_cant_puntaje =  py.transform.scale(icono_cant_puntaje,(70,40))
    PANTALLA.blit(icono_cant_puntaje,(20,150))
    puntaje = fuente.render(str(spiderman.puntaje),True,AZUL,ROJO)
    PANTALLA.blit(puntaje,(100,150))
    
    #TIEMPO DE DISPARO SPIDER-MAN
    tiempo_actual = py.time.get_ticks()
    teclas = py.key.get_pressed()
    
    if teclas[py.K_f] and bandera_disparo ==True and spiderman.vida >0:
        if spiderman.que_hace  == "Derecha" or spiderman.que_hace =="Quieto" and spiderman.cant_telarañas !=0 :
            if tiempo_actual - tiempo_ultimo_disparo >= 500 :
                spiderman.lanzar_telaraña()
                spiderman.cant_telarañas = spiderman.cant_telarañas - 1
                tiempo_ultimo_disparo = tiempo_actual
        if spiderman.que_hace  == "Izquierda" or spiderman.ultimo_movimiento  == "Izquierda" :
            if tiempo_actual - tiempo_ultimo_disparo >= 500 and spiderman.cant_telarañas !=0:
                spiderman.lanzar_telaraña()
                spiderman.cant_telarañas = spiderman.cant_telarañas - 1
                tiempo_ultimo_disparo = tiempo_actual
    
    #VIDA LIZARD
    if scorpion.vida == 0 and scorpion_dos.vida ==0 and bandera_aparece_lizard == True:
        texto_lizard = fuente.render(str(lizard.vida),False,VERDE,VIOLETA)
        icono_lizard = py.image.load(r"spiderman_game\Recursos\lizard\vida-lizard.png")
        icono_lizard = py.transform.scale(icono_lizard,(70,70))
        PANTALLA.blit(icono_lizard,(1000,20))
        PANTALLA.blit(texto_lizard,(920,30))

    if scorpion.vida != 0 :
        spiderman.verificar_colision_enemigo_dos(scorpion, PANTALLA)
    if scorpion_dos.vida !=0 :
        spiderman.verificar_colision_enemigo_dos(scorpion_dos, PANTALLA)
    if lizard.vida !=0:
        spiderman.verificar_colision_enemigo_dos(lizard, PANTALLA)
    spiderman.colision_telaraña(lista_enemigos,PANTALLA)
    spiderman.verificar_colision_simbionte(simbionte)
    spiderman.actualizar(PANTALLA, plataformas)
    
    scorpion.actualizar(PANTALLA)
    scorpion_dos.actualizar(PANTALLA)
    if scorpion.vida ==0 and scorpion_esta_muerto == False:
        spiderman.puntaje +=250
        scorpion_esta_muerto = True
    if scorpion_dos.vida == 0 and scorpion_dos_esta_muerto == False:
        spiderman.puntaje +=250
        scorpion_dos_esta_muerto = True
    if lizard.vida == 0 and lizard_esta_muerto== False:
        spiderman.puntaje += 1000
        lizard_esta_muerto = True
    if scorpion.vida == 0 and scorpion_dos.vida ==0:
        bandera_aparece_lizard = True
    if bandera_aparece_lizard == True:
        lizard.actualizar(PANTALLA)
    
    tiempo_game_over = py.time.get_ticks()
    
    #CREANDO OBJETOS
    primer_objeto.blitear_objeto(PANTALLA)
    segundo_objeto.blitear_objeto(PANTALLA)
    if spiderman.rectangulo_principal.colliderect(primer_objeto.rectangulo_principal) and primer_objeto.agarrado == False:
        spiderman.cant_telarañas = spiderman.cant_telarañas + 10
        spiderman.puntaje -= 100
        primer_objeto.agarrado = True
        
    if spiderman.rectangulo_principal.colliderect(segundo_objeto.rectangulo_principal) and segundo_objeto.agarrado == False:
        spiderman.vida = spiderman.vida + 30
        segundo_objeto.agarrado = True
        spiderman.puntaje -= 100
    if spiderman.vida > 100:
        spiderman.vida = 100
    if spiderman.cant_telarañas > 50:
        spiderman.cant_telarañas = 50
    if spiderman.puntaje < 0:
        spiderman.puntaje =0
    if spiderman.vida == 0:
        
        tiempo_actual_derrota = py.time.get_ticks()#Tiempo en milisegundos desde que iniciamos el juego.
        tiempo_actual_derrota += tiempo_actual_derrota + 1 
        tiempo_transcurrido =tiempo_actual_derrota# calculamos el tiempo transcurrido.
        tiempo_final_derrota =tiempo_transcurrido*0.001
        if tiempo_final_derrota > 50:
            cartel_game_over = py.image.load(r"spiderman_game\Recursos\fondos\fondo-game-over.png")
            cartel_game_over = py.transform.scale(cartel_game_over,(1220,720))
            PANTALLA.blit(cartel_game_over,(0,-35))
            puntaje = fuente.render(str(spiderman.puntaje),True,AZUL,ROJO)
            PANTALLA.blit(puntaje,(1050,250))
    if tiempo>60 and lizard.vida !=0:
        cartel_game_over = py.image.load(r"spiderman_game\Recursos\fondos\fondo-game-over.png")
        cartel_game_over = py.transform.scale(cartel_game_over,(1220,720))
        PANTALLA.blit(cartel_game_over,(0,-35))
        puntaje = fuente.render(str(spiderman.puntaje),True,AZUL,ROJO)
        PANTALLA.blit(puntaje,(1050,250))
        supero_tiempo = fuente.render("Superaste el limite",True,AZUL,ROJO)
        supero_tiempo_dos = fuente.render("de tiempo.",True,AZUL,ROJO)
        PANTALLA.blit(supero_tiempo,(950,500))
        PANTALLA.blit(supero_tiempo_dos,(990,539))
    
    
    
    

    py.display.update()

py.quit()