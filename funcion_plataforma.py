import pygame as py

def crear_plataforma(pantalla,visible,esPremio,esMovil, tamaño,  x,  y:int,path=""):
    plataforma = {}
    eje_y = y
    movimiento_sube = True
    if visible and esMovil == False:
        plataforma["superficie"] = py.image.load(path)
        plataforma["superficie"] = py.transform.scale(plataforma["superficie"], tamaño)
        pantalla.blit(plataforma["superficie"],(x,eje_y))
        plataforma["rectangulo"] = plataforma["superficie"].get_rect()
        plataforma["rectangulo"].x = x
        plataforma["rectangulo"].y = y
    if visible and esMovil:
        if movimiento_sube == True:
            eje_y = eje_y - 10
            plataforma["superficie"] = py.image.load(path)
            plataforma["superficie"] = py.transform.scale(plataforma["superficie"], tamaño)
            pantalla.blit(plataforma["superficie"],(x,eje_y))
            plataforma["rectangulo"] = plataforma["superficie"].get_rect()
            plataforma["rectangulo"].x = x
            plataforma["rectangulo"].y = eje_y
        if eje_y < 200:
            movimiento_sube = False
        if movimiento_sube == False:
            eje_y=eje_y +120
            plataforma["superficie"] = py.image.load(path)
            plataforma["superficie"] = py.transform.scale(plataforma["superficie"], tamaño)
            pantalla.blit(plataforma["superficie"],(x,eje_y))
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
def crear_plataforma_movil(pantalla,visible,esPremio,esMovil, tamaño,  x,  y:int,path=""):
    plataforma = {}
    global eje_y 
    global movimiento_sube
    if visible and esMovil == False:
        plataforma["superficie"] = py.image.load(path)
        plataforma["superficie"] = py.transform.scale(plataforma["superficie"], tamaño)
        pantalla.blit(plataforma["superficie"],(x,eje_y))
        plataforma["rectangulo"] = plataforma["superficie"].get_rect()
        plataforma["rectangulo"].x = x
        plataforma["rectangulo"].y = eje_y
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
            pantalla.blit(plataforma["superficie"],(x,eje_y))
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
            pantalla.blit(plataforma["superficie"],(x,eje_y))
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


