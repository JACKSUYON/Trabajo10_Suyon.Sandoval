import libreria
# Menu  tienda de ferreteria
def Clavos():
    nombre=libreria.pedir_nombre("ingrese nombre:")
    contenido=nombre + "\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print(" Se guardaron datos")
    print("")
def Alambre():
    nombre=libreria.pedir_nombre("ingrese nombre:")
    contenido=nombre + "\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print(" Se guardaron datos")
    print("")
def Fierro():
    nombre=libreria.pedir_nombre("ingrese nombre:")
    contenido=nombre + "\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print(" Se guardaron datos")
    print("")
def Cemento():
    nombre=libreria.pedir_nombre("ingrese nombre:")
    contenido=nombre + "\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print(" Se guardaron datos")
    print("")
def Calamina():
    nombre=libreria.pedir_nombre("ingrese nombre:")
    contenido=nombre + "\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print(" Se guardaron datos")
    print("")

def obtenerdatos_Ferreteria():
    datos=libreria.obtener_datos("info.txt")
    if (datos != ""):
        print(datos)
    else:
        print("no encontramos nada en ferreteria")
opc=0
max=7
while (opc!=max):
    print("####### Menu Ferreteria #######")
    print("1.Clavos                       ")
    print("2.Alambre                      ")
    print("3.Fierro                       ")
    print("4.Cemento                      ")
    print("5.Calamina                     ")
    print("6.Obtener datos                ")
    print("7.Salir                        ")


    opc=libreria.pedir_numero("ingrese opcion:",1,6)
    # Mapeo de las opciones
    if (opc == 1):
        Clavos()
    if (opc == 2):
        Alambre()
    if (opc == 3):
        Fierro()
    if (opc == 4):
        Cemento()
    if (opc == 5):
        Calamina()
    if (opc == 6):
        obtenerdatos_Ferreteria()
    # fin_if
# fin_while
print("fin del programa.........")
