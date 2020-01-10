import libreria
# Menu de hoteles
def HotelPuertoelSol():
    nombre=libreria.pedir_nombre("ingrese nombre:")
    contenido=nombre + "\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print("SE GUARDARON DATOS")
    print("")
def HotelCasaAndinaSelect():
    nombre=libreria.pedir_nombre("ingrese nombre:")
    contenido=nombre + "\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print("SE GUARDARON DATOS")
    print("")
def HotelAmerica():
    nombre=libreria.pedir_nombre("ingrese nombre:")
    contenido=nombre + "\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print("SE GUARDARON DATOS")
    print("")
def LeerDatos_Agregados():
    leer=libreria.obtener_datos("info.txt")
    if (leer !=""):
        print(leer)
    else:
        print("NO SE AGREGARON NADA ")
    # fin_if
# fin_def
opc=0
max=5
while(opc!=max):
    print("##### Menu Hotel #####")
    print("1.Puerto del Sol      ")
    print("2.Casa Andina Select  ")
    print("3.America             ")
    print("4.leer datos          ")
    print("5.Salir               ")
    print("######################")

    opc=libreria.pedir_numero("ingrese opcion:",1,4)


    if (opc==1):
        HotelPuertoelSol()
    if (opc==2):
        HotelCasaAndinaSelect()
    if (opc==3):
        HotelAmerica()
    if (opc ==4):
        LeerDatos_Agregados()
    # fin_if
# fin_while
print("fin del programa .........")
