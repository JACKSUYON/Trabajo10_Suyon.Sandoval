import libreria
# Submenu de Marcas de Zapatillas
def MarcaAdidas():
    print("se eligio marca Adidas ")
    print("")
def MarcaNike():
    print("se eligio marca Nike   ")
    print("")
def MarcaPuma():
    print("se eligio marca Puma    ")
    print("")
def submenu_marcas1():
    opc=0
    max=4
    while(opc!=max):
        print("####### Menu Marcas #####")
        print("1.Adidas                 ")
        print("2.Nike                   ")
        print("3.Puma                   ")
        print("4.Salir                  ")

        opc=libreria.pedir_numero("ingrese opcion:",1,4)

        if (opc==1):
            MarcaAdidas()
        if (opc==2):
            MarcaNike()
        if (opc==3):
            MarcaPuma()
        # fin_if
    #fin_while
# fin_def

def submenu_marcas2():
    opc=0
    max=4
    while(opc!=max):
        print("####### Menu Marcas #####")
        print("1.Adidas                 ")
        print("2.Nike                   ")
        print("3.Puma                   ")
        print("4.Salir                  ")

        opc=libreria.pedir_numero("ingrese opcion:",1,4)

        if (opc==1):
            MarcaAdidas()
        if (opc==2):
            MarcaNike()
        if (opc==3):
            MarcaPuma()
        #fin_if
    #fin_while
#fin_def
opc=0
max=3
while (opc != max):
    print("###### Menu ###########")
    print("1. Elegir marca 1      ")
    print("2. Elegir marca 2      ")
    print("3. salir               ")

    opc=libreria.pedir_numero("ingrese opcion:",1,3)

    if (opc == 1):
        submenu_marcas1()
    if (opc == 2):
        submenu_marcas2()
    # fin_if
#fin_while
print("fin del programa ..........")
