import libreria
# Menu de Ofertas
def ofertas1():
    print("opcion: eligio la oferta 1")
def ofertas2():
    print("opcion: eligio la oferta 2")

def ofertas3():
    print("opcion: eligio la oferta 3")
def submenu_polos():
    opc=0
    max=4
    while (opc != max):
        # MENU
        print("#####################")
        print("###### ofertas en Polos #####")
        print("1.oferta1 4*3 ,paga 30 soles  ")
        print("2.oferta2 3*2,paga 20 soles   ")
        print("3.oferta3 5*3,paga 60 soles   ")
        print("4.Salir                       ")
        print("##############################")

        opc=libreria.pedir_numero("ingrese opcion:",1,4)
        # Mapeo de opciones

        if (opc == 1):
            ofertas1()
        if (opc == 2):
            ofertas2()
        if (opc == 3):
            ofertas3()
        # fin_if
    #fin_while
#fin_def
def submenu_pantalones():
    opc=0
    max=4
    while (opc != max):
        print("#####################")
        print("####### ofertas en Pantalones #####")
        print("1.oferta1 4*3 ,paga 50 soles  ")
        print("2.oferta2 3*2,paga 40 soles   ")
        print("3.oferta3 5*3,paga 80 soles   ")
        print("4.Salir                       ")
        print("##############################")

        opc=libreria.pedir_numero("ingrese opcion:",1,4)

        if (opc == 1):
            ofertas1()
        if (opc == 2):
            ofertas2()
        if (opc == 3):
            ofertas3()
        #fin_if
    # fin_while
# fin_def
opc=0
max=3
while (opc != max):
    print("###########################")
    print("########Menu###############")
    print("1.Ofertas de Polos         ")
    print("2.Ofertas de pantalones    ")
    print("3.salir                    ")
    print("###########################")

    opc=libreria.pedir_numero("ingrese opcion:",1,3)

    if (opc == 1):
        submenu_polos()
    if (opc == 2):
        submenu_pantalones()
    # fin_if
# fin_while
print("fin del programa .......")
