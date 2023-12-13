import pygame as py

def reescalar_imagenes(diccionario_animaciones, ancho, alto):
    for clave in diccionario_animaciones:
        for i in range(len(diccionario_animaciones[clave])):
            img = diccionario_animaciones[clave][i]
            diccionario_animaciones[clave][i] = py.transform.scale(img, (ancho,alto))

def rotar_imagen(imagenes:list):
    lista_imagenes = []
    for i in range(len(imagenes)):
        imagen_rotada = py.transform.flip(imagenes[i],True,False)
        lista_imagenes.append(imagen_rotada)
    
    return lista_imagenes

super_mario =[py.image.load(r"mario-bros\Recursos\0.png")]

personaje_quieto = [py.image.load(r"spiderman_game\Recursos\spider-man\quieto.png")]
personaje_quieto_izquierda = rotar_imagen(personaje_quieto)
personaje_camina_derecha = [py.image.load(r"spiderman_game\Recursos\spider-man\derecha-1.png"),
                            py.image.load(r"spiderman_game\Recursos\spider-man\derecha-2.png"),
                            py.image.load(r"spiderman_game\Recursos\spider-man\derecha-3.png"),
                            py.image.load(r"spiderman_game\Recursos\spider-man\derecha-4.png"),
                            py.image.load(r"spiderman_game\Recursos\spider-man\derecha-5.png")]
personaje_camina_izquierda = rotar_imagen(personaje_camina_derecha)

personaje_dispara_izquierda = [py.image.load(r"spiderman_game\Recursos\spider-man\dispara.png")]
personaje_dispara_derecha = rotar_imagen(personaje_dispara_izquierda)
personaje_salta = [py.image.load(r"spiderman_game\Recursos\spider-man\salto-2.png")]
personaje_derrotado = [py.image.load(r"spiderman_game\Recursos\spider-man\derrotado-7.png")]

personaje_cae = [py.image.load(r"spiderman_game\Recursos\spider-man\salto-5.png")]

personaje_golpea_derecha = [py.image.load(r"spiderman_game\Recursos\spider-man\golpe.png")]
personaje_golpea_izquierda = rotar_imagen(personaje_golpea_derecha)

enemigo_camina = [py.image.load(r"spiderman_game\Recursos\lizard\corre-1.png"), py.image.load(r"spiderman_game\Recursos\lizard\corre-2.png"),py.image.load(r"spiderman_game\Recursos\lizard\corre-3.png"),
py.image.load(r"spiderman_game\Recursos\lizard\corre-4.png"),
py.image.load(r"spiderman_game\Recursos\lizard\corre-5.png"),
py.image.load(r"spiderman_game\Recursos\lizard\corre-6.png"),
py.image.load(r"spiderman_game\Recursos\lizard\corre-7.png"),
py.image.load(r"spiderman_game\Recursos\lizard\corre-8.png"),]

enemigo_camina_derecha = rotar_imagen(enemigo_camina)

enemigo_quieto = [py.image.load(r"spiderman_game\Recursos\lizard\derrotado-1.png"),py.image.load(r"spiderman_game\Recursos\lizard\derrotado-2.png"),
py.image.load(r"spiderman_game\Recursos\lizard\derrotado-3.png"),
py.image.load(r"spiderman_game\Recursos\lizard\derrotado-4.png"),
py.image.load(r"spiderman_game\Recursos\lizard\derrotado-5.png"),
py.image.load(r"spiderman_game\Recursos\lizard\derrotado-6.png")]

enemigo_derrotado_1 = [py.image.load(r"spiderman_game\Recursos\lizard\derrotado-6.png")]

enemigo_golpeado = [py.image.load(r"spiderman_game\Recursos\lizard\derrotado-4.png")]

venom_camina_derecha = [py.image.load(r"spiderman_game\Recursos\venom\venom-corre-1.png"),
py.image.load(r"spiderman_game\Recursos\venom\venom-corre-2.png"),
py.image.load(r"spiderman_game\Recursos\venom\venom-corre-3.png"),
py.image.load(r"spiderman_game\Recursos\venom\venom-corre-4.png"),
py.image.load(r"spiderman_game\Recursos\venom\venom-corre-5.png"),
py.image.load(r"spiderman_game\Recursos\venom\venom-corre-6.png")]

venom_camina_izquierda = rotar_imagen(venom_camina_derecha)

venom_quieto = [py.image.load(r"spiderman_game\Recursos\venom\venom-quieto.png")]

venom_derrotado_1 = [py.image.load(r"spiderman_game\Recursos\venom\venom-derrotado.png")]

hobgoblin_camina_derecha = [py.image.load(r"spiderman_game\Recursos\hob-goblin\mueve-1.png"),
                            py.image.load(r"spiderman_game\Recursos\hob-goblin\mueve-2.png")]

hobgoblin_camina_izquierda = rotar_imagen(hobgoblin_camina_derecha)

hobgoblin_derrotado = [py.image.load(r"spiderman_game\Recursos\hob-goblin\derrotado.png")]

greengoblin_mueve = [py.image.load(r"spiderman_game\Recursos\green-goblin\mueve.png")]

greengoblin_derrotado = [py.image.load(r"spiderman_game\Recursos\green-goblin\derrotado.png")]

scorpion_camina_derecha = [py.image.load(r"spiderman_game\Recursos\scorpion\corre-1.png"),
                            py.image.load(r"spiderman_game\Recursos\scorpion\corre-2.png"),
                            py.image.load(r"spiderman_game\Recursos\scorpion\corre-3.png"),
                            py.image.load(r"spiderman_game\Recursos\scorpion\corre-4.png"),
                            py.image.load(r"spiderman_game\Recursos\scorpion\corre-5.png"),
                            py.image.load(r"spiderman_game\Recursos\scorpion\corre-6.png"),]



scorpion_camina_izquierda = rotar_imagen(scorpion_camina_derecha)

scorpion_derrotado = [py.image.load(r"spiderman_game\Recursos\scorpion\derrotado.png")]

#ELECTRO

electro_derrotado = [py.image.load(r"spiderman_game\Recursos\electro\derrotado_3.png")]

electro_quieto = [py.image.load(r"spiderman_game\Recursos\electro\electro_quieto.png")]

electro_dispara = [py.image.load(r"spiderman_game\Recursos\electro\electro_dispara_1.png"),
                    py.image.load(r"spiderman_game\Recursos\electro\electro_dispara_2.png"),
                    py.image.load(r"spiderman_game\Recursos\electro\electro_dispara_3.png"),
                    py.image.load(r"spiderman_game\Recursos\electro\electro_dispara_4.png")]

electro_disparo = [py.image.load(r"spiderman_game\Recursos\electro\disparo_izquierda.png")]

#SPIDER-MAN TRAJE NEGRO
spiderblack_derecha = [py.image.load(r"spiderman_game\Recursos\spider-man-black\corre-1.png"),
py.image.load(r"spiderman_game\Recursos\spider-man-black\corre-2.png"),
py.image.load(r"spiderman_game\Recursos\spider-man-black\corre-3.png"),
py.image.load(r"spiderman_game\Recursos\spider-man-black\corre-4.png"),
py.image.load(r"spiderman_game\Recursos\spider-man-black\corre-5.png")]

spiderblack_izquierda = rotar_imagen(spiderblack_derecha)

spiderblack_quieto = [py.image.load(r"spiderman_game\Recursos\spider-man-black\quieto.png")]

spiderblack_quieto_izquierda = rotar_imagen(spiderblack_quieto)

spiderblack_derrotado = [py.image.load(r"spiderman_game\Recursos\spider-man-black\derrotado.png")]

spiderblack_salta = [py.image.load(r"spiderman_game\Recursos\spider-man-black\salta.png")]

spiderblack_golpea_derecha =[py.image.load(r"spiderman_game\Recursos\spider-man-black\golpea.png")]
spiderblack_golpea_izquierda = rotar_imagen(spiderblack_golpea_derecha)

#OBJETOS 
recarga_telaraña = [py.image.load(r"spiderman_game\Recursos\spider-man\telaraña.png")]

bola_simbionte=[py.image.load(r"spiderman_game\Recursos\objetos\simbionte-3.png")]

incremento_vida = [py.image.load(r"spiderman_game\Recursos\objetos\corazon.png")]