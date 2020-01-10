import libreria
# Menu de Entrada al almuerzo
def EntradaSopa():
    print("opcion: eligio de entrada sopa")
def EntradaCeviche():
    print("opcion: eligio de entrada ceviche")
def EntradaPapaHuancaina():
    print("opcion: eligio de entrada papa huancaina")
def submenu_entrada_Arroz_Pato():
    opc=0
    max=4
    while(opc!=max):
        print("#######Menu Entrada#######")
        print("1.Sopa                    ")
        print("2.Ceviche                 ")
        print("3.Papa Huancaína          ")
        print("4.salir                   ")
        print("##########################")

        opc=libreria.pedir_numero("ingrese opcion:",1,4)

        if (opc == 1):
            EntradaSopa()
        if (opc == 2):
            EntradaCeviche()
        if (opc == 3):
            EntradaPapaHuancaina()

def submenu_entrada_Seco_Cabrito():
    opc=0
    max=4
    while(opc!=max):
        print("#######Menu Entrada#######")
        print("1.Sopa                    ")
        print("2.Ceviche                 ")
        print("3.Papa Huancaína          ")
        print("4.salir                   ")
        print("##########################")

        opc=libreria.pedir_numero("ingrese opcion:",1,4)
        # Mapeo de opciones
        if (opc == 1):
            EntradaSopa()
        if (opc == 2):
            EntradaCeviche()
        if (opc == 3):
            EntradaPapaHuancaina()
        # fin_if
    #fin_while
#fin_def
opc=0
max=3
while (opc != max):
    print("##### Menu #########")
    print("1.Arroz con Pato    ")
    print("2.Seco de Cabrito   ")
    print("3.Salir             ")
    print("####################")

    opc=libreria.pedir_numero("ingrese opcion:",1,3)
    # mapeo de opciones
    if (opc == 1):
        submenu_entrada_Arroz_Pato()
    if (opc == 2):
        submenu_entrada_Seco_Cabrito()
    # fin_if
# fin_while

print("fin del programa ...........")

