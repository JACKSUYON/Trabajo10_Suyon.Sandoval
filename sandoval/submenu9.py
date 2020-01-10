import libreria
# Submenu de Hotel
def HotelPuertoelSol():
    print("eligio Hotel Puerto el Sol")
    print("")
def HotelCasaAndinaSelect():
    print("eligio Casa Andina Select")
    print("")
def HotelAmerica():
    print("eligio Hotel America     ")
    print("")
# Maria elige Hotel ?
def submenu_Maria_hotel():
    opc=0
    max=4
    while(opc!=max):
        print("##### Menu Hotel #####")
        print("1.Puerto del Sol      ")
        print("2.Casa Andina Select  ")
        print("3.America             ")
        print("4.Salir               ")

        opc=libreria.pedir_numero("ingrese opcion:",1,4)


        if (opc==1):
            HotelPuertoelSol()
        if (opc==2):
            HotelCasaAndinaSelect()
        if (opc==3):
            HotelAmerica()
        #fin_if
    #fin_while
#fin_def

# Jose elige hotel ?
def submenu_Jose_hotel():
    opc=0
    max=4
    while(opc!=max):
        print("##### Menu Hotel #####")
        print("1.Puerto del Sol      ")
        print("2.Casa Andina Select  ")
        print("3.America             ")
        print("4.Salir               ")

        opc=libreria.pedir_numero("ingrese opcion:",1,4)

        if (opc==1):
            HotelPuertoelSol()
        if (opc==2):
            HotelCasaAndinaSelect()
        if (opc==3):
            HotelAmerica()
        # fin_if
    # fin_while
# fin_def
opc=0
max=3
while (opc != max):
    print("#########################")
    print("1.Maria elige hotel:     ")
    print("2.Jose elige hotel:      ")
    print("3.salir                  ")
    print("#########################")

    opc=libreria.pedir_numero("ingrese opcion:",1,3)

    if (opc == 1):
        submenu_Maria_hotel()
    if (opc == 2):
        submenu_Jose_hotel()
    #fin_if
# fin_def
