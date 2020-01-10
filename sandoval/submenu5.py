import libreria
#Menu de jugadores
def Gano1000punto():
    print("gano 10000 puntos ")
def Gano800punto():
    print("gano 8000 puntos  ")
def Perdio():
    print("Perdio el juego   ")
def jugador1():
    opc=0
    max=4
    while (opc != max):
        print("#####################")
        print("####### Menu ########")
        print("1.Gano 10000 puntos  ")
        print("2.Gano 800 puntos    ")
        print("3.Perdio             ")
        print("4.salir              ")

        opc=libreria.pedir_numero("ingrese opcion:",1,4)
        # Mapeo de las opciones

        if (opc == 1):
            Gano1000punto()
        if (opc == 2):
            Gano800punto()
        if (opc == 3):
           Perdio()
        # fin_if
    # fin_while
#fin_def
def jugador2():
    opc=0
    max=4
    while (opc != max):
        print("#####################")
        print("####### Menu ########")
        print("1.Gano 10000 puntos  ")
        print("2.Gano 800 puntos    ")
        print("3.Perdio             ")
        print("4.salir              ")

        opc=libreria.pedir_numero("ingrese opcion:",1,4)
        # Mapeo de las opciones
        if (opc == 1):
            Gano1000punto()
        if (opc == 2):
            Gano800punto()
        if (opc == 3):
            Perdio()
        # fin_if
    # fin_while
# fin_def
opc=0
max=3
while (opc != max):
    print("########################")
    print("#######Menu#############")
    print("1. Jugador 1            ")
    print("2. Jugador 2            ")
    print("3. salir                ")
    print("########################")

    opc=libreria.pedir_numero("ingrese opcion:",1,3)

    if (opc == 1):
        jugador1()
    if (opc == 2):
        jugador2()
    if (opc == 3):
        Perdio()
    # fin_if
# fin_while
print("fin del programa .......")
