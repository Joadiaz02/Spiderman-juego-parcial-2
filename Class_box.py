import pygame as py

class box:

    def __init__(self,surface,posicion,path=None) :
        if path == None:
            self.image = py.Surface(surface)
        else:
            self.image = py.image.load(path)
            self.image = py.transform.scale(self.image,surface)
        
        self.rect = self.image.get_rect()
        self.rect.x = posicion[0]
        self.rect.y = posicion[1]