import libreria
# Submenu de configuracion celulares
def configPantalla():
    print("opcion: eligio config pantalla")
    print("")
def configPlaca():
    print("opcion: eligio conf Placa     ")
    print("")
def configAudio():
    print("opcion: eligio config Audio   ")
    print("")
def submenu_tecnico_Juan():

    opc=0
    max=4
    while (opc != max):
        print("###########################")
        print("####### conf Celular ######")
        print("1.conf Pantalla            ")
        print("2.conf Placa               ")
        print("3.conf Audio               ")
        print("4. salir                   ")
        print("###########################")

        opc=libreria.pedir_numero("ingrese opcion:",1,4)

        if (opc == 1):
            configPantalla()
        if (opc == 2):
            configPlaca()
        if (opc == 3):
             configAudio()
        #fin_if
    # fin_while
#fin_def
def submenu_tecnico_Elmer():
    opc=0
    max=4
    while (opc != max):
        print("###########################")
        print("####### conf Celular ######")
        print("1.conf Pantalla            ")
        print("2.conf Placa               ")
        print("3.conf Audio               ")
        print("4. salir                   ")
        print("###########################")

        opc=libreria.pedir_numero("ingrese opcion:",1,4)

        if (opc == 1):
            configPantalla()
        if (opc == 2):
            configPlaca()
        if (opc == 3):
            configAudio()
        #fin_if
    #fin_while
#fin_def
opc=0
max=3
while (opc != max):
    print("##############################")
    print("######## Menu Tecnico ########")
    print("1.Tecnico Juan  (carco)       ")
    print("2.Tecnico Elmer (chato)       ")
    print("3.salir                       ")
    print("##############################")

    opc=libreria.pedir_numero("ingrese opcion:",1,3)

    if (opc == 1):
        submenu_tecnico_Juan()
    if (opc == 2):
        submenu_tecnico_Elmer()
    #fin_if
# fin_while
print("fin del programa ..............")
