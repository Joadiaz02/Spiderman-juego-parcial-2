from GUI.UI.GUI_form import *
from GUI.UI.GUI_button_image import *
from GUI.UI.GUI_form_contenedor_nivel import *
from manejador_niveles import Manejador_niveles
import pygame as py
from pygame.locals import *
from archivos.funciones import *
class FormMenuPlay(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border, active,path_image):
        super().__init__(screen, x, y, w, h, color_background, color_border, active)
        self.manejador_niveles = Manejador_niveles(self._master)
        aux_image = py.image.load(path_image)
        aux_image= py.transform.scale(aux_image,(w,h))
        self._slave = aux_image

        #self.btn = Button_Image(screen= self._slave,master_x= x, master_y=y,x=100,y=100,w=100,h=150,path_image=r"",)
        partidas=lectura_partida_json()
        
        self._btn_level_1 = Button_Image(screen=self._slave,master_x=x,master_y=y,x=100,y=100,w=100,h=150,path_image=r"spiderman_game\GUI\Recursos\nivel_uno.png",onclick = self.entrar_nivel,onclick_param="nivel_uno")
        if partidas["Termino_nivel_uno"]== True:
            self._btn_level_2 = Button_Image(screen=self._slave,x=250,y=100,master_x=x,master_y=y,w=100,h=150,path_image=r"spiderman_game\GUI\Recursos\nivel_dos.png",onclick = self.entrar_nivel,onclick_param="nivel_dos")
            self.lista_widgets.append(self._btn_level_2)
        if partidas["Termino_nivel_dos"]== True:
            self._btn_level_3 = Button_Image(screen=self._slave,x=100,y=250,master_x=x,master_y=y,w=100,h=150,path_image=r"spiderman_game\GUI\Recursos\nivel_tres.png",onclick = self.entrar_nivel,onclick_param="nivel_tres",text="",font="Verdana",font_size=15,font_color=(0,255,0),color_background=(255,0,0),color_border=(255,0,255))
            self.lista_widgets.append(self._btn_level_3)

        self._btn_home = Button_Image(screen=self._slave,x=400,y=400,master_x=x,master_y=y,w=50,h=50,path_image=r"spiderman_game\GUI\Recursos\home.png",onclick = self.btn_home_click,onclick_param="")
        
        self.lista_widgets.append(self._btn_level_1)
        
        
        self.lista_widgets.append(self._btn_home)
        
    def on(self,parametro):
        print("hola,parametro")
        
    def update(self,lista_eventos):
        if self.verificar_dialog_result():
            for widget in self.lista_widgets:
                widget.update(lista_eventos)
            self.draw()
        else:
            self.hijo.update(lista_eventos)
        
    def entrar_nivel(self,nombre_nivel):
        nivel = self.manejador_niveles.get_nivel(nombre_nivel)
        frm_contenedor_nivel= FormContenedorNivel(self._master,nivel)
        self.show_dialog(frm_contenedor_nivel)

    def btn_home_click(self,param):
        self.end_dialog()