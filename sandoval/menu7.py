import libreria
# Menu de marcas de Autos
def Honda():
    nombre=libreria.pedir_nombre("ingrese nombre:")
    contenido=nombre + "\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print("SE GUARDARON DATOS")
    print("")
def Hyundai():
    nombre=libreria.pedir_nombre("ingrese nombre:")
    contenido=nombre + "\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print(" SE GUARDARON DATOS")
    print("")
def Bugatti():
    nombre=libreria.pedir_nombre("ingrese nombre:")
    contenido=nombre + "\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print("SE GUARDARON DATOS")
    print("")
def Toyota():
    nombre=libreria.pedir_nombre("ingrese nombre:")
    contenido=nombre + "\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print("SE GUARDARON DATOS")
    print("")
def obtenerDatos():
    nombre=libreria.obtener_datos("info.txt")
    if (nombre != ""):
        print(nombre)
    else:
        print(" NO CONTIENE DATOS")
opc=0
max=6
while(opc!=max):
    print("###### Menu Marcas de Auto######")
    print("1.Honda                         ")
    print("2.Hyundai                       ")
    print("3.Bugatti                       ")
    print("4.Toyota                        ")
    print("5.obtener Datos")
    print("6.Salir                         ")

    opc=libreria.pedir_numero("ingrese opcion:",1,5)

    if (opc==1):
        Honda()
    if (opc==2):
        Hyundai()
    if (opc==3):
        Bugatti()
    if (opc==4):
        Toyota()
    if (opc == 5):
        obtenerDatos()
    # fin_if
# fin_while

print("fin del programa............")


