import libreria
# Menu de licores
def RonCortavio():
    print("opcion: eligio Ron Cortavio  ")
    print("")
def Tequila():
    print("opcion: eligio  Tequila    ")
    print("")
def Whisky():
    print("opcion: eligio Whisky   ")
    print("")
def submenu_licor1():
    opc=0
    max=4
    while (opc != max):
        print("##### Menu licor #######")
        print("1.Ron Cortavio          ")
        print("2.Tequila               ")
        print("3.Whisky                ")
        print("4.Salir                 ")

        opc=libreria.pedir_numero("ingrese opcion:",1,4)

        if (opc==1):
            RonCortavio()
        if (opc == 2):
            Tequila()
        if (opc == 3):
            Whisky()
        # fin_if
    # fin_while
#fin_def

def submenu_licor2():
    opc=0
    max=4
    while (opc != max):
        print("##### Menu licor #######")
        print("1.Ron Cortavio          ")
        print("2.Tequila               ")
        print("3.Whisky                ")
        print("4.Salir                 ")

        opc=libreria.pedir_numero("ingrese opcion:",1,4)

        if (opc==1):
            RonCortavio()
        if (opc == 2):
            Tequila()
        if (opc == 3):
            Whisky()
        # fin_if
    #fin_while
#fin_def
opc=0
max=3
while (opc != max):
    print("#######################")
    print("###### Menu ###########")
    print("1.Ingrese Licor 1      ")
    print("2.Ingrese Licor 2      ")
    print("3.salir                ")
    print("#######################")

    opc=libreria.pedir_numero("ingrese opcion:",1,3)

    if (opc == 1):
        submenu_licor1()
    if (opc == 2):
        submenu_licor2()
    # fin_if
#fin_while
print("fin del programa .........")
