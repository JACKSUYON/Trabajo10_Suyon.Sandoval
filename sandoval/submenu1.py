import libreria
# Inplementacion de Sub menu
def verduraApio():
    print("ingreso verdura apio      ")
def verduraCebolla():
    print("ingreso verdura cebolla")
def verduraLechuga():
    print("ingrese verdura Lechuga  ")
def submenu_opcion_verduras():
    opc=0
    max=4
    while (opc != max):
        print("############################")
        print("####### Menu Verduras#######")
        print("1.Apio                      ")
        print("2.Cebolla                   ")
        print("3.Lechuga                   ")
        print("4.sali                      ")

        opc=libreria.pedir_numero("ingrese opcion:",1,4)

        if (opc == 1):
            verduraApio()
        if (opc == 2):
            verduraCebolla()
        if (opc == 3):
            verduraLechuga()

def submenu_opcion_verdura2():
    opc=0
    max=4
    while (opc != max):
        print("############################")
        print("####### Menu Verduras#######")
        print("1.Apio                      ")
        print("2.Cebolla                   ")
        print("3.Lechuga                   ")
        print("4.sali                      ")

        opc=libreria.pedir_numero("ingrese opcion:",1,4)

        if (opc == 1):
            verduraApio()
        if (opc == 2):
            verduraCebolla()
        if (opc == 3):
            verduraLechuga()
        # fin_if
    #fin_while
#fin_def
opc=0
max=3
while (opc !=max ):
    print("######## Menu ##########")
    print("1.ingrese verduras 1")
    print("2. ingrese verduras 2")
    print("3.salir              ")

    opc=libreria.pedir_numero("ingrese opcion:",1,3)
    #Mapeo de las opciones
    if (opc == 1):
        submenu_opcion_verduras()
    if (opc == 2):
        submenu_opcion_verdura2()
    # fin_if
#fin_while
print("fin del programa")
