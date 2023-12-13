import pygame
from pygame.locals import *
import sqlite3

from GUI.UI.GUI_textbox import *
from GUI.UI.GUI_slider import *
from GUI.UI.GUI_button import *

from GUI.UI.GUI_label import *
from GUI.UI.GUI_form import *
from GUI.UI.GUI_button_image import *
from GUI.UI.GUI_form_menu_play import *
from GUI.UI.GUI_form_menu_score import *
from archivos.funciones import *
from GUI.UI.GUI_configuraciones import *


    
class FormPrueba(Form):
    def __init__(self, screen, x,y,w,h,color_background, color_border = "Black", border_size = -1, active = True):
        super().__init__(screen, x,y,w,h,color_background, color_border, border_size, active)
        
        self.nombre_uno=""
        self.nombre_dos = ""
        self.puntaje_uno = ""
        self.puntaje_dos = ""
        self.flag_play = True
        

        self.volumen = 0.1
        pygame.mixer.init()
        pygame.mixer.music.load(r"spiderman_game\GUI\Recursos\musica_menu_spidy.mp3")
        pygame.mixer.music.set_volume(self.volumen)
        pygame.mixer.music.play(-1)

        self.txt_nombre = TextBox(self._slave,x,y,50,500,150,50,"blue","black","red","grey", 3,"Comic Sans MS",15,"white")#_slave seria la pantalla
        nombre_jugador_texto=self.txt_nombre.get_text()
        #self.txt_nombre.set_text(nombre_jugador_texto)
        
        escribir_usuario("joaco",100)

        self.btn_play = Button(self._slave,x,y,650,450,100,50,"blue","red",self.btn_play_click,"PLAY","PAUSE","Verdana",15,"white")
        self.btn_nueva_partida = Button(self._slave,x,y,50,20,130,50,"blue","red",self.btn_nueva_partida_click,"NUEVA PARTIDA","NUEVA PARTIDA","Verdana",15,"white")
        self.btn_nuevo_usuario = Button(self._slave,x,y,50,130,130,50,"blue","red",self.btn_nuevo_usuario_click,"NUEVO USUARIO","NUEVO USUARIO","Verdana",15,"white")
        self.slider_volumen = Slider(self._slave,x,y,100,400,500,15,self.volumen,"blue","white")
        porcentaje_volumen= f"{self.volumen * 100}%"
        self.label_volumen = Label(self._slave,650,380,100,50,porcentaje_volumen,"Comic Sans MS",15,"white",r"spiderman_game\GUI\Recursos\Table.png")

        self.btn_tabla = Button_Image(self._slave,x,y,270,480,100,100,r"spiderman_game\GUI\Recursos\boton_ranking.png",self.btn_tabla_click,"")
        self.btn_jugar = Button_Image(self._slave,x,y,450,490,100,70,r"spiderman_game\GUI\Recursos\play.png",self.btn_jugar_click,"a")
        self.btn_botones = Button_Image(self._slave,x,y,1050,580,60,60,r"spiderman_game\Recursos\ruedita_config.png",self.btn_botones_click,"")

        self.lista_widgets.append(self.txt_nombre)
        self.lista_widgets.append(self.btn_play)
        self.lista_widgets.append(self.slider_volumen)
        self.lista_widgets.append(self.label_volumen)
        self.lista_widgets.append(self.btn_tabla)
        self.lista_widgets.append(self.btn_jugar)
        self.lista_widgets.append(self.btn_botones)
        self.lista_widgets.append(self.btn_nueva_partida)
        self.lista_widgets.append(self.btn_nuevo_usuario)
    def render(self):
        self._slave.fill(self._color_background)
        spiderman_menu=pygame.image.load(r"spiderman_game\GUI\Recursos\spiderman.png")
        spiderman_menu= pygame.transform.scale(spiderman_menu,(300,550))
        self._slave.blit(spiderman_menu,(800,-30))
        spiderman_title = pygame.image.load(r"spiderman_game\GUI\Recursos\spiderman_title.png")
        spiderman_title = pygame.transform.scale(spiderman_title,(450,150))
        self._slave.blit(spiderman_title,(300,20))

    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                self.draw()
                self.render()
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)
                self.update_volumen(lista_eventos)
                
        else:
            self.hijo.update(lista_eventos)

    def update_volumen(self, lista_eventos):
        self.volumen = self.slider_volumen.value
        self.label_volumen.update(lista_eventos)
        self.label_volumen.set_text(f"{round(self.volumen * 100)}%")
        pygame.mixer.music.set_volume(self.volumen)
        
    def btn_nueva_partida_click(self,param):
        escribir_partida_json(False,False,False,0,0,0)
        #escribir_nombre_json("")
        cartel_partida_creada = py.image.load(r"spiderman_game\GUI\Recursos\texto_partida_creada.png")
        cartel_partida_creada = py.transform.scale(cartel_partida_creada,(140,80))
        self._slave.blit(cartel_partida_creada,(50,60))
        

    def btn_nuevo_usuario_click(self,param):
        escribir_nombre_json("")
        cartel_partida_creada = py.image.load(r"spiderman_game\GUI\Recursos\texto_partida_creada.png")
        cartel_partida_creada = py.transform.scale(cartel_partida_creada,(140,80))
        self._slave.blit(cartel_partida_creada,(50,170))
        #input("Ingrese su nombre: ")
    def btn_play_click(self, param):
        if self.flag_play == True:
            pygame.mixer.music.pause()
            self.btn_play._color_background = "black"
            self.btn_play.set_text("PLAY")
        else:
            pygame.mixer.music.unpause()
            self.btn_play._color_background = "blue"
            self.btn_play.set_text("PAUSE")
            
        self.flag_play = not self.flag_play
    
    def btn_jugar_click(self,param):
        frm_jugar = FormMenuPlay(screen=self._master,x = self._master.get_width()/2-250, y = self._master.get_height()/2-250, w=500,h=500,color_background=(220,0,220),color_border=(255,255,255),active = True,path_image=r"spiderman_game\GUI\Recursos\Window.png")
        self.show_dialog(frm_jugar)
    def btn_tabla_click(self, param):
        with sqlite3.connect(r"spiderman_game\archivos\base_de_datos.db") as conexion:
            try:
                sentencia = 'select * from ranking order by puntaje desc limit 3 '
                cursor = conexion.execute(sentencia)
                cursor = list(cursor)
                print(cursor)
                
                self.nombre_uno=cursor[0]
                self.nombre_dos = cursor[1]
                self.nombre_tres = cursor[2]
                print(self.nombre_uno)
                
            except IndexError:
                print("ERROR!!!")
        diccionario=[{"jugador": str(self.nombre_uno[0]), "score": str(self.nombre_uno[1])},{"jugador": str(self.nombre_dos[0]), "score": str(self.nombre_dos[1])},{"jugador": self.nombre_tres[0], "score": self.nombre_tres[1]}]
        nuevo_form = FormMenuScore(screen = self._master,x=250,y=25,w=500,h=550,color_background="red",color_border="blue", active=True, path_image=r"spiderman_game\GUI\Recursos\Window.png",scoreboard= diccionario,margen_x=10,margen_y=100,espacio=10)
        self.show_dialog(nuevo_form)

    def btn_botones_click(self, param):
        
        nuevo_form_botones = FormMenuConfig(screen = self._master,x=250,y=25,w=500,h=550,color_background="red",color_border="blue", active=True, path_image=r"spiderman_game\GUI\Recursos\menu-configuraciones.png",scoreboard= "",margen_x=10,margen_y=100,espacio=10)
        self.show_dialog(nuevo_form_botones)
