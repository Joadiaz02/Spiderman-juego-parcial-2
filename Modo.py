DEBUG = False

def cambiar_modo():
    global DEBUG
    DEBUG = not DEBUG

def obtener_modo():
    return DEBUG