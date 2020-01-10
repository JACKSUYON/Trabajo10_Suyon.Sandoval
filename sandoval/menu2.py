import libreria
# Menu de verduras
def opcion1():
    nombre=libreria.pedir_nombre("ingrese nombre:")
    contenido=nombre + "\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print("SE GUARDARON DATOS")
    print("")
def opcion2():
    nombre=libreria.pedir_nombre("ingrese nombre:")
    contenido=nombre + "\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print("SE GUARDARON DATOS")
    print("")
def opcion3():
    nombre=libreria.pedir_nombre("ingrese nombre:")
    contenido=nombre + "\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print("SE GUARDARON DATOS")
    print("")
def LeerDatos_verduras():
    verduras=libreria.obtener_datos("info.txt")
    if (verduras != ""):
        print(verduras)
    else:
        print("No contiene Archivo  ")
    #fin_if

opc=0
max=5
while (opc !=max):
    print("####### Menu Verduras ###########")
    print("1.opcion 1                       ")
    print("2.Opcion 2                       ")
    print("3.Opcion 3                       ")
    print("4.leer datos                     ")
    print("5.Salir                          ")
    print("#################################")


    opc = libreria.pedir_numero("ingrese opcion:",1,4)

    # mapeo
    if (opc == 1):
       opcion1()
    if (opc == 2):
        opcion2()
    if (opc == 3):
        opcion3()
    if (opc == 4):
        LeerDatos_verduras()
    # fin_if
#fin_while

print ("Fin del programa ..........")
