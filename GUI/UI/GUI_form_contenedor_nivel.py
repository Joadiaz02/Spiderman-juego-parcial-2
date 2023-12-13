from GUI.UI.GUI_form import *
from GUI.UI.GUI_button_image import *
from GUI.UI.GUI_label import *
from GUI.UI.GUI_button import *
from GUI.UI.GUI_slider import *
import pygame as py
from pygame.locals import *

class FormContenedorNivel(Form):
    def __init__(self, PANTALLA: py.Surface, nivel):
        super().__init__(PANTALLA,0,0,PANTALLA.get_width(),PANTALLA.get_height())
        nivel._slave = self._slave
        self.nivel = nivel
        self._btn_home = Button_Image(screen=self._slave,x=self._w-50,y=self._h-50,master_x=self._x,master_y=self._y,w=50,h=50,path_image=r"spiderman_game\GUI\Recursos\home.png",onclick = self.btn_home_click,onclick_param="")
        #self._btn_pause = Button_Image(screen=self._slave,x=1100,y=20,master_x=self._x,master_y=self._y,w=50,h=50,path_image=r"spiderman_game\GUI\Recursos\boton_pausa.png",onclick = self.btn_pause_click,onclick_param="")
        self.lista_widgets.append(self._btn_home)
        #self.lista_widgets.append(self._btn_pause)
        self.flag_play = True
        self.volumen = 0.7
        pygame.mixer.init()
        pygame.mixer.music.load(r"spiderman_game\GUI\Recursos\musica_menu_spidy.mp3")
        pygame.mixer.music.set_volume(self.volumen)
        pygame.mixer.music.play(-1)
        porcentaje_volumen= f"{self.volumen * 100}%"

        self.label_volumen = Label(self._slave,650,380,100,50,porcentaje_volumen,"Comic Sans MS",15,"white",r"spiderman_game\GUI\Recursos\Table.png")
        self.btn_play = Button(self._slave,self._x,self._y,10,200,80,30,"blue","red",self.btn_play_click,"MUSIC ON","MUSIC OFF","Verdana",15,"white")
        self.lista_widgets.append(self.btn_play)
        self.slider_volumen = Slider(self._slave,self._x,self._y,10,240,70,15,self.volumen,"blue","white")
        self.lista_widgets.append(self.slider_volumen)
    def update(self, lista_eventos):
        self.nivel.update(lista_eventos)
        for widget in self.lista_widgets:
            widget.update(lista_eventos)
        self.draw()
        self.update_volumen(lista_eventos)
    
    def btn_home_click(self,param):
        self.end_dialog()
        self.end_dialog()

    def btn_play_click(self, param):
        if self.flag_play == True:
            pygame.mixer.music.pause()
            self.btn_play._color_background = "black"
            self.btn_play.set_text("MUSIC ON")
        else:
            pygame.mixer.music.unpause()
            self.btn_play._color_background = "blue"
            self.btn_play.set_text("MUSIC OFF")
            
        self.flag_play = not self.flag_play

    
    def update_volumen(self, lista_eventos):
        self.volumen = self.slider_volumen.value
        self.label_volumen.update(lista_eventos)
        self.label_volumen.set_text(f"{round(self.volumen * 100)}%")
        pygame.mixer.music.set_volume(self.volumen)
    #def btn_pause_click(self,param):
    #    logo_pausa = py.image.load(r"spiderman_game\Recursos\boton_pausa.png")
    #    logo_pausa = py.transform.scale(logo_pausa,(300,200))
    #    self._slave.blit(logo_pausa,(500,300))
    #    self.end_dialog()