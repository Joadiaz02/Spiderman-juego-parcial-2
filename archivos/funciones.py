import json
import csv

imprimir = lambda mensaje:print(mensaje)

def lectura_partida_json():
    '''
    Funcion: Lee un archivo en formato JSON.
    Retorna: Los datos que contiene el archivo JSON.
    '''
    try:
        with open(r'spiderman_game\archivos\partidas.json','r') as archivo_partidas:
            cadena_json = json.load(archivo_partidas)
            return cadena_json
    except FileNotFoundError:
        imprimir("Archivo no encontrado")


def lectura_nombre_json():
    '''
    Funcion: Lee un archivo en formato JSON.
    Retorna: Los datos que contiene el archivo JSON.
    '''
    try:
        with open(r'spiderman_game\archivos\nombres.json','r') as archivo_nombres:
            cadena_json = json.load(archivo_nombres)
            return cadena_json
    except FileNotFoundError:
        imprimir("Archivo no encontrado")

def escribir_nombre_json(nombre:str):
    '''
    Funcion: Escribe un nombre recibido por parametro en un archivo JSON.
    Parametros: Recibe por parametro un nombre.
    '''
    try:
        termino_partida ={'Nombre_usuario':nombre}
        with open(r'spiderman_game\archivos\nombres.json','w',encoding='utf-8') as archivo_nombres:

            json.dump(termino_partida,archivo_nombres,indent=4)
    except FileNotFoundError:
        imprimir("Archivo no encontrado")

def escribir_partida_json(termino_partida_uno:bool,termino_partida_dos:bool,termino_partida_tres:bool,puntaje_uno:int,puntaje_dos:int,puntaje_tres:int):
    '''
    Funcion: Escribe un nombre recibido por parametro en un archivo JSON.
    Parametros: Recibe por parametro un nombre.
    '''
    try:
        termino_partida ={'Termino_nivel_uno':termino_partida_uno,'Termino_nivel_dos':termino_partida_dos,'Termino_nivel_tres':termino_partida_tres,'puntaje_nivel_uno':puntaje_uno,'puntaje_nivel_dos':puntaje_dos,'puntaje_nivel_tres':puntaje_tres}
        with open(r'spiderman_game\archivos\partidas.json','w',encoding='utf-8') as archivo_partidas:

            json.dump(termino_partida,archivo_partidas,indent=4)
    except FileNotFoundError:
        imprimir("Archivo no encontrado")

def lectura_usuarios_json():
    '''
    Funcion: Lee un archivo en formato JSON.
    Retorna: Los datos que contiene el archivo JSON.
    '''
    with open(r'spiderman_game\archivos\usuarios.json','r') as archivo_usuarios:
        cadena_json = json.load(archivo_usuarios)
        return cadena_json

def escribir_usuario(usuario,puntaje):
    usuario ={'usuario':usuario,'puntaje':puntaje}
    with open(r'spiderman_game\archivos\usuarios.json','w',encoding='utf-8') as archivo_usuarios:
        json.dump(usuario,archivo_usuarios,indent=4)

hola = escribir_usuario("cuty",1000)
print(hola)
#def lectura_puntajes():
#    puntajes= ''
#    with open(r'spiderman_game\archivos\usuarios.csv', newline='') as archivo_puntajes:
#        
#        data = csv.reader(archivo_puntajes,delimiter=',')
#        puntajes = list(data)
#        return puntajes

#def escribir_puntajes(nombre,puntaje,puntajes:list):
#    for usuario in range(len(puntajes)):
#        puntajes.append(nombre)
#    with open(r'spiderman_game\archivos\usuarios.csv', newline='') as archivo_puntajes:
#        writer= csv.writer(archivo_puntajes,delimiter=',')
#        writer.writerows(puntajes)

#puntajes = lectura_puntajes()
#hola = escribir_puntajes("matias",100,puntajes)

