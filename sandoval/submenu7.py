import libreria
# Submenu de Canciones
def EnseniameSoniar():
    print("opcion: eligio Enseñamme a soñar ")
    print("")
def BailaConmigo():
    print("opcion: eligio Baila Conmigo    ")
    print("")
def AloneAlanWalker():
    print("opcion: eligio Alone            ")
    print("")
def submenu_elegir_musica1():
    opc=0
    max=4
    while (opc != max):
        print("##### Menu Canciones #######")
        print("1.Enseñame a soñar          ")
        print("2.Baila Conmigo             ")
        print("3.Alone                     ")
        print("4.Salir                     ")

        opc=libreria.pedir_numero("ingrese opcion:",1,4)

        if (opc==1):
            EnseniameSoniar()
        if (opc == 2):
            BailaConmigo()
        if (opc == 3):
            AloneAlanWalker()
        # fin_if
    # fin_while
# fin_def
def submenu_elegir_cancion2():
    opc=0
    max=4
    while (opc != max):
        print("##### Menu Canciones #######")
        print("1.Enseñame a soñar          ")
        print("2.Baila Conmigo             ")
        print("3.Alone                     ")
        print("4.Salir                     ")

        opc=libreria.pedir_numero("ingrese opcion:",1,4)

        if (opc==1):
            EnseniameSoniar()
        if (opc == 2):
            BailaConmigo()
        if (opc == 3):
            AloneAlanWalker()
        # fin_if
    #fin_while
#fin_def

opc=0
max=3
while (opc != max):
    print("#######################")
    print("###### Menu ###########")
    print("1.Ingrese Musica 1     ")
    print("2.Ingrese Musica 2     ")
    print("3.salir                ")
    print("#######################")

    opc=libreria.pedir_numero("ingrese opcion:",1,3)

    if (opc == 1):
        submenu_elegir_musica1()
    if (opc == 2):
        submenu_elegir_cancion2()
    #fin_if
# fin_while
print("fin del programa .........")
