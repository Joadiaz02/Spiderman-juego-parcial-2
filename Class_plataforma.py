import pygame as py

class plataforma:
    #lizard = Enemigo(diccionario_animaciones_lizard,1200,535,"izquierda",primera_tope_izquierda,primera_tope_derecha,PANTALLA)
    def __init__(self, visible,esPremio,esMovil,tamaño, x,y,path,pantalla) -> None:
        self.visible = visible
        self.esPremio = esPremio
        self.esMovil = esMovil
        self.tamaño = tamaño
        self.pos_x = x
        self.pos_y = y
        self.path = path
        self.pantalla = pantalla
        






    def crear_plataforma(self):
        plataforma = {}
        
        movimiento_sube = True
        if self.visible and self.esMovil == False:
            plataforma["superficie"] = py.image.load(self.path)
            plataforma["superficie"] = py.transform.scale(plataforma["superficie"], self.tamaño)
            self.pantalla.blit(plataforma["superficie"],(self.pos_x,self.pos_y))
        if self.visible and self.esMovil:
            if movimiento_sube == True:
                self.pos_y = self.pos_y - 10
                plataforma["superficie"] = py.image.load(self.path)
                plataforma["superficie"] = py.transform.scale(plataforma["superficie"], self.tamaño)
                self.pantalla.blit(plataforma["superficie"],(self.pos_x,self.pos_y))
            
            if self.pos_y < 200:
                movimiento_sube = False
            if movimiento_sube == False:
                self.pos_y=self.pos_y +10
                plataforma["superficie"] = py.image.load(self.path)
                plataforma["superficie"] = py.transform.scale(plataforma["superficie"], self.tamaño)
                self.pantalla.blit(plataforma["superficie"],(self.pos_x,self.pos_y))
            if self.pos_y > 600:
                movimiento_sube = True


        else:
            plataforma["superficie"] = py.Surface(self.tamaño)

        plataforma["rectangulo"] = plataforma["superficie"].get_rect()
        plataforma["rectangulo"].x = self.pos_x
        plataforma["rectangulo"].y = self.pos_y
        plataforma["premio"] = self.esPremio
        #return plataforma