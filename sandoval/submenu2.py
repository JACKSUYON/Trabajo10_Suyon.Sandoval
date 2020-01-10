import libreria
# Menu configuracion de autos
def configAuto_Android():
    print("opcion: Android Auto elegida")
    print("")
def confgAuto_FarosLed():
    print("opcion: Faros Led elegida   ")
    print("")
def configAutos_Potencia500Hp():
    print("opcion: Potencia 500 HP elegida")
    print("")
def submenu_opcion_confgToyota():
    opc=0
    max=4
    while(opc!=max):
        print("###### Config Autos ########")
        print("1.conf Android Auto         ")
        print("2.conf Faros led            ")
        print("3.Potencia de 550 HP        ")
        print("4.Exit                      ")

        opc=libreria.pedir_numero("ingrese opcion:",1,4)

        if (opc == 1):
            configAuto_Android()
        if (opc == 2):
            confgAuto_FarosLed()
        if (opc == 3):
            configAutos_Potencia500Hp()
        # fin_if
    #fin_while

def submenu_opcion_confgHonda():
    opc=0
    max=4
    while(opc!=max):
        print("###### Config Autos ########")
        print("1.conf Android Auto         ")
        print("2.conf Faros led            ")
        print("3.Potencia de 550 HP        ")
        print("4.Exit                      ")

        opc=libreria.pedir_numero("ingrese opcion:",1,4)

        if (opc == 1):
            configAuto_Android()
        if (opc == 2):
            confgAuto_FarosLed()
        if (opc == 3):
            configAutos_Potencia500Hp()
        # fin_if
    #fin_while
#fin_def

opc=0
max=3
while (opc!=max):
    print("###### Config Autos #########")
    print("1.confg Toyota               ")
    print("2.config Honda               ")
    print("3.Exit                       ")

    opc=libreria.pedir_numero("ingrese opcion:",1,3)

    if (opc == 1):
        submenu_opcion_confgToyota()
    if (opc == 2):
        submenu_opcion_confgHonda()
    #fin_if
#fin_while
print("fin del programa..........")
