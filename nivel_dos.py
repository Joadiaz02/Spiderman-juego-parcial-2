import pygame as py
from pygame.locals import *
from Configuraciones import *
from os import system
system("cls")
from Class_Personaje import Personaje
from Modo import *
from Class_enemigo import Enemigo
from Class_objeto import Objeto
from Class_disparo import disparo
ROJO = (255,0,0)
AZUL = (0,0,255)
VIOLETA =(120,40,140)
VERDE=(100,255,0)
BLANCO = (255,255,255)
NEGRO = (0,0,0)
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
            plataforma["rectangulo"].y  -= 10
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
            plataforma["rectangulo"].y  += 10
            PANTALLA.blit(plataforma["superficie"],(x,eje_y))
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
fondo = py.image.load(r"spiderman_game\Recursos\fondos\fondo-2.jfif").convert()#acelera el juego y hace que consuma menos recursos
fondo = py.transform.scale(fondo, (W,H))



#contador_pasos = 0

diccionario = {}
diccionario_black ={}
diccionario["Quieto"] = personaje_quieto
diccionario["Quieto_izquierda"] = personaje_quieto_izquierda
diccionario["Derecha"] = personaje_camina_derecha
diccionario["Izquierda"] = personaje_camina_izquierda
diccionario["Salta"] = personaje_salta
diccionario["cae"] = personaje_cae
diccionario["derrotado"] = personaje_derrotado

diccionario_black["Derecha"] = spiderblack_derecha
diccionario_black["Izquierda"] = spiderblack_izquierda
diccionario_black["Quieto_izquierda"] = spiderblack_quieto_izquierda
diccionario_black["Quieto"] = spiderblack_quieto
diccionario_black["Salta"] = spiderblack_salta
diccionario_black["derrotado"] = spiderblack_derrotado
diccionario_black["dispara_izquierda"] = personaje_dispara_izquierda
diccionario_black["dispara_derecha"] = personaje_dispara_derecha
diccionario_black["cae"] = personaje_cae

diccionario["dispara_izquierda"] = personaje_dispara_izquierda
diccionario["dispara_derecha"] = personaje_dispara_derecha
diccionario_recibido = diccionario
spiderman = Personaje(diccionario_recibido,(70,60),600,350,20,100,50,0,PANTALLA)
reescalar_imagenes(diccionario, 100,90)
reescalar_imagenes(diccionario_black, 100,90)
#OBJETOS
diccionario_objetos = {"cartucho": recarga_telaraña, "corazon": incremento_vida,"simbionte": bola_simbionte}

primer_objeto = Objeto(diccionario_objetos,"cartucho",1010,200)
segundo_objeto = Objeto(diccionario_objetos,"corazon",1120,440)
tercer_objeto = Objeto(diccionario_objetos,"simbionte",320,400)

#PLATAFORMAS
piso = crear_plataforma(True,False,False, (820,20), 0, 480, r"spiderman_game\Recursos\fondos\fondo-1.jpg")
plataforma_invisible = crear_plataforma(True,False,False,(370,20),930,530,r"spiderman_game\Recursos\fondos\fondo-1.jpg")

plataforma_invisible_2 = crear_plataforma(True,False,False,(160,20),910,280,r"spiderman_game\Recursos\fondos\fondo-1.jpg")
premio = crear_plataforma(False,True,False,(60,50),1200,410,"")
plataforma_invisible_3 = crear_plataforma(False,False,False,(290,20),530,280,r"mario-bros\Recursos\fondo.png")
plataforma_invisible_4 = crear_plataforma(False,False,False,(300,20),50,280,r"mario-bros\Recursos\fondo.png")
plataforma_diagonal_abajo = crear_plataforma(False,False,False,(70,10),820,490,r"mario-bros\Recursos\fondo.png")
plataforma_diagonal_arriba = crear_plataforma(False,False,False,(70,10),1060,230,r"mario-bros\Recursos\fondo.png")
plataforma_diagonal_arriba_dos = crear_plataforma(False,False,False,(70,10),1130,200,r"mario-bros\Recursos\fondo.png")
plataforma_diagonal_arriba_tres = crear_plataforma(False,False,False,(70,10),1200,230,r"mario-bros\Recursos\fondo.png")
zona_dispara_electro = crear_plataforma(False,False,False,(348,201),278,149,r"mario-bros\Recursos\fondo.png")

#Topes
primera_tope_izquierda = crear_plataforma(False,False,False,(10,40),50,265,r"mario-bros\Recursos\fondo.png")
primera_tope_derecha = crear_plataforma(False,False,False,(10,40),350,265,r"mario-bros\Recursos\fondo.png")
segundo_tope_izquierda = crear_plataforma(False,False,False,(10,40),530,275,r"mario-bros\Recursos\fondo.png")
segundo_tope_derecha = crear_plataforma(False,False,False,(10,40),815,275,r"mario-bros\Recursos\fondo.png")
tercer_tope_izquierda = crear_plataforma(False,False,False,(10,40),0,410,r"mario-bros\Recursos\fondo.png")
tercer_tope_derecha = crear_plataforma(False,False,False,(10,40),750,410,r"mario-bros\Recursos\fondo.png")

#plataforma_movil_nivel_uno = crear_plataforma_movil(True,False,True,(100,20),50,eje_y,r"spiderman_game\Recursos\fondos\planeador.png")

plataformas= [piso,plataforma_invisible_2,plataforma_diagonal_abajo,plataforma_diagonal_arriba,plataforma_diagonal_arriba_tres,plataforma_diagonal_arriba_dos ,plataforma_invisible,premio,plataforma_invisible_3,plataforma_invisible_4]





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
        elif event.type == KEYDOWN:
            if event.key == K_TAB:
                cambiar_modo()

    teclas = py.key.get_pressed()

    if teclas[py.K_RIGHT] and spiderman.animacion_actual != spiderman.animaciones["derrotado"]:
        spiderman.que_hace = "Derecha"
        bandera_disparo = True
        spiderman.ultimo_movimiento = "Derecha"
    elif teclas[py.K_LEFT] and spiderman.animacion_actual != spiderman.animaciones["derrotado"]:
        spiderman.que_hace = "Izquierda"
        bandera_disparo = True
        spiderman.ultimo_movimiento = "Izquierda"
    elif(teclas[py.K_SPACE]) and spiderman.animacion_actual != spiderman.animaciones["derrotado"]:
        spiderman.que_hace = "Salta"
        bandera_disparo = True
    elif spiderman.animacion_actual != spiderman.animaciones["derrotado"]:
        if spiderman.ultimo_movimiento == "Derecha":
            spiderman.que_hace = "Quieto"
        if spiderman.ultimo_movimiento == "Izquierda":
            spiderman.que_hace = "Quieto_izquierda"
        bandera_disparo = True
    #elif spiderman.vida == 0:
    #    spiderman.que_hace = "derrotado"
    fuente = py.font.SysFont("Arial",30)
    PANTALLA.blit(fondo,(0,0))

    
    #plataforma_movil_nivel_uno = crear_plataforma_movil(True,False,True,(100,50),50,eje_y,r"spiderman_game\Recursos\fondos\planeador.png")
    trampa = crear_plataforma(True,False,False,(180,20),540,308,r"spiderman_game\Recursos\objetos\trampa.png")
    if spiderman.rectangulo_principal.colliderect(trampa["rectangulo"]):
        spiderman.rectangulo_principal.y += 100
        spiderman.puntaje -= 50
        spiderman.vida = spiderman.vida -20
    #plataforma_movil = py.image.load(r"spiderman_game\Recursos\fondos\planeador.png")
    #plataforma_movil = py.transform.scale(plataforma_movil, (100,40))
    #PANTALLA.blit(plataforma_movil,(100,500))
    tiempo = py.time.get_ticks()/1000
    tiempo = int(tiempo)
    if aux == tiempo:
        aux +=1
    contador = fuente.render("Tiempo : "+str(tiempo),True,AZUL,ROJO)
    PANTALLA.blit(contador,(550,20))


    #CANTIDAD DE TELARAÑAS
    texto_cant_telarañas = fuente.render(str(spiderman.cant_telarañas),False,AZUL,ROJO)
    icono_cant_telarañas = py.image.load(r"spiderman_game\Recursos\spider-man\telaraña.png")
    icono_cant_telarañas =  py.transform.scale(icono_cant_telarañas,(70,70))
    PANTALLA.blit(icono_cant_telarañas,(20,90))
    PANTALLA.blit(texto_cant_telarañas,(100,105))
    #TIEMPO DE DISPARO SPIDER-MAN
    #spiderman.gastar_telaraña(PANTALLA,AZUL,ROJO,fuente)

    icono_cant_puntaje = py.image.load(r"spiderman_game\Recursos\fondos\score.png")
    icono_cant_puntaje =  py.transform.scale(icono_cant_puntaje,(70,40))
    PANTALLA.blit(icono_cant_puntaje,(20,150))
    puntaje = fuente.render(str(spiderman.puntaje),True,AZUL,ROJO)
    PANTALLA.blit(puntaje,(100,150))

    #VIDA SPIDER-MAN
    
    texto_spiderman = fuente.render(str(spiderman.vida),False,AZUL,ROJO)
    icono_spiderman = py.image.load(r"spiderman_game\Recursos\spider-man\vida-logo.png")
    icono_spiderman = py.transform.scale(icono_spiderman,(70,70))
    PANTALLA.blit(icono_spiderman,(20,30))
    PANTALLA.blit(texto_spiderman,(100,30))
    if tercer_objeto.agarrado == True:
        icono_spiderman = py.image.load(r"spiderman_game\Recursos\spider-man-black\logo.png")
        icono_spiderman = py.transform.scale(icono_spiderman,(70,70))
        PANTALLA.blit(icono_spiderman,(20,30))
        texto_spiderman = fuente.render(str(spiderman.vida),False,BLANCO,NEGRO)
        PANTALLA.blit(texto_spiderman,(100,30))
        texto_cant_telarañas = fuente.render(str(spiderman.cant_telarañas),False,BLANCO,NEGRO)
        icono_cant_telarañas = py.image.load(r"spiderman_game\Recursos\spider-man\telaraña.png")
        icono_cant_telarañas =  py.transform.scale(icono_cant_telarañas,(70,70))
        PANTALLA.blit(icono_cant_telarañas,(20,90))
        PANTALLA.blit(texto_cant_telarañas,(100,105))
        icono_cant_puntaje = py.image.load(r"spiderman_game\Recursos\spider-man-black\score-black.png")
        icono_cant_puntaje =  py.transform.scale(icono_cant_puntaje,(70,40))
        PANTALLA.blit(icono_cant_puntaje,(20,150))
        puntaje = fuente.render(str(spiderman.puntaje),True,BLANCO,NEGRO)
        PANTALLA.blit(puntaje,(100,150))
    

    
    
    tiempo_actual = py.time.get_ticks()
    teclas = py.key.get_pressed()
    
    if teclas[py.K_f] and bandera_disparo ==True and spiderman.vida >0 and  spiderman.cant_telarañas !=0:
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
        if tercer_objeto.agarrado == True:
            if spiderman.que_hace  == "Derecha" or spiderman.que_hace =="Quieto" and spiderman.cant_telarañas !=0 :
                if tiempo_actual - tiempo_ultimo_disparo >= 200 :
                    spiderman.lanzar_telaraña()
                    spiderman.cant_telarañas = spiderman.cant_telarañas - 1
                    tiempo_ultimo_disparo = tiempo_actual
            if spiderman.que_hace  == "Izquierda" or spiderman.ultimo_movimiento  == "Izquierda" :
                if tiempo_actual - tiempo_ultimo_disparo >= 200 and spiderman.cant_telarañas !=0:
                    spiderman.lanzar_telaraña()
                    spiderman.cant_telarañas = spiderman.cant_telarañas - 1
                    tiempo_ultimo_disparo = tiempo_actual
    
    #spiderman.verificar_estado_spiderman(PANTALLA)
    #VIDA VENOM
    if scorpion.vida == 0 and scorpion_dos.vida ==0 and bandera_aparece_venom == True:
        texto_venom = fuente.render(str(venom.vida),False,BLANCO,AZUL)
        icono_venom = py.image.load(r"spiderman_game\Recursos\venom\venom-vida.png")
        icono_venom = py.transform.scale(icono_venom,(70,70))
        PANTALLA.blit(icono_venom,(1000,20))
        PANTALLA.blit(texto_venom,(920,30))

    #PANTALLA.blit(plataforma_caño["superficie"], plataforma_caño["rectangulo"])
    #if simbionte["descubierta"] == True and simbionte["tocada"]==False:
    #    PANTALLA.blit(simbionte["superficie"], simbionte["rectangulo"])
    if scorpion.vida != 0 :
        spiderman.verificar_colision_enemigo_dos(scorpion, PANTALLA)
    if scorpion_dos.vida !=0 :
        spiderman.verificar_colision_enemigo_dos(scorpion_dos, PANTALLA)
    if venom.vida !=0:
        spiderman.verificar_colision_enemigo_dos(venom, PANTALLA)
    spiderman.colision_telaraña(lista_enemigos,PANTALLA)
    #spiderman.verificar_colision_simbionte(simbionte)
    spiderman.actualizar(PANTALLA, plataformas)
    #for enemigo in lista_enemigos:
    #    enemigo.actualizar(PANTALLA)
    
    scorpion.actualizar(PANTALLA)
    scorpion_dos.actualizar(PANTALLA)
    
    if scorpion.vida ==0 and scorpion_esta_muerto == False:
        spiderman.puntaje +=250
        scorpion_esta_muerto = True
    if scorpion_dos.vida == 0 and scorpion_dos_esta_muerto == False:
        spiderman.puntaje +=250
        scorpion_dos_esta_muerto = True
    if venom.vida == 0 and venom_esta_muerto== False:
        spiderman.puntaje += 1000
        venom_esta_muerto = True
    
    if scorpion.vida == 0 and scorpion_dos.vida ==0:
        bandera_aparece_venom = True
    
    if bandera_aparece_venom == True:
        venom.actualizar(PANTALLA)
        if tiempo_actual - tiempo_ultimo_disparo >= 500  and venom.vida !=0:
            venom.lanzar_simbionte()
            tiempo_ultimo_disparo = tiempo_actual
            
    venom.colision_simbionte(spiderman,PANTALLA)
    if venom.vida ==0:
        tercer_objeto.blitear_objeto(PANTALLA)
        if spiderman.rectangulo_principal.colliderect(tercer_objeto.rectangulo_principal) and tercer_objeto.agarrado == False:
            spiderman = Personaje(diccionario_black,(70,60),600,350,20,200,100,spiderman.puntaje,PANTALLA)
            reescalar_imagenes(diccionario_black, 100,90)
            tercer_objeto.agarrado = True
        #f tercer_objeto.agarrado == True:
            spiderman.vida = 200
            spiderman.cant_telarañas = 100
    #electro.actualizar_dos(PANTALLA)
    #spiderman.verificar_colision_activa_disparo(zona_dispara_electro,850,200,electro,PANTALLA)
    
    
    
    
        #electro.actualizar(PANTALLA)
    
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
    if spiderman.vida > 100 and tercer_objeto.agarrado != True:
        spiderman.vida = 100
    if spiderman.cant_telarañas > 50 and tercer_objeto.agarrado != True:
        spiderman.cant_telarañas = 50
    if spiderman.puntaje < 0:
        spiderman.puntaje = 0
    if spiderman.vida == 0:
        
        tiempo_actual_derrota = py.time.get_ticks()#Tiempo en milisegundos desde que iniciamos el juego.
        tiempo_actual_derrota += tiempo_actual_derrota + 1 
        tiempo_transcurrido =tiempo_actual_derrota# calculamos el tiempo transcurrido.
        tiempo_final_derrota =tiempo_transcurrido*0.001
        if tiempo_final_derrota > 50 :
            cartel_game_over = py.image.load(r"spiderman_game\Recursos\fondos\fondo-game-over.png")
            cartel_game_over = py.transform.scale(cartel_game_over,(1220,720))
            PANTALLA.blit(cartel_game_over,(0,-35))
            puntaje = fuente.render(str(spiderman.puntaje),True,AZUL,ROJO)
            PANTALLA.blit(puntaje,(1050,250))
    if tiempo>60 and venom_esta_muerto != True:
        cartel_game_over = py.image.load(r"spiderman_game\Recursos\fondos\fondo-game-over.png")
        cartel_game_over = py.transform.scale(cartel_game_over,(1220,720))
        PANTALLA.blit(cartel_game_over,(0,-35))
        puntaje = fuente.render(str(spiderman.puntaje),True,AZUL,ROJO)
        PANTALLA.blit(puntaje,(1050,250))
        supero_tiempo = fuente.render("Superaste el limite",True,AZUL,ROJO)
        supero_tiempo_dos = fuente.render("de tiempo.",True,AZUL,ROJO)
        PANTALLA.blit(supero_tiempo,(950,500))
        PANTALLA.blit(supero_tiempo_dos,(990,539))
    
    
    if obtener_modo():
        
        #py.draw.rect(PANTALLA, "yellow", piso, 3)
        #py.draw.rect(PANTALLA, "blue", spiderman.left_box.rect.left,3)
        #py.draw.rect(PANTALLA, "red", mario.rectangulo_principal_abajo,3)
        py.draw.rect(PANTALLA, "blue", spiderman.rectangulo_principal,3)
        py.draw.rect(PANTALLA, "blue", primer_objeto.rectangulo_principal,3)
        py.draw.rect(PANTALLA, "blue", segundo_objeto.rectangulo_principal,3)
        py.draw.rect(PANTALLA, "red", primera_tope_izquierda["rectangulo"],3)
        py.draw.rect(PANTALLA, "blue",primera_tope_derecha["rectangulo"],3)
        py.draw.rect(PANTALLA, "blue", venom.rectangulo_principal,3)
        #py.draw.rect(PANTALLA, "blue", spiderman.rectangulo_principal_derecha,3)
        for plataforma in plataformas:
            py.draw.rect(PANTALLA, "red", plataforma["rectangulo"], 3)
        py.draw.rect(PANTALLA,"blue",zona_dispara_electro["rectangulo"],3)
        
    py.display.update()

py.quit()