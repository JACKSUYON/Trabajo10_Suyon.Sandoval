import libreria
# Menu de marcas de Zapatillas
def MarcaAdidas():
    nombre=libreria.pedir_nombre("ingrese nombre:")
    contenido=nombre + "\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print(" Se guardaron datos")
    print("")
def MarcaNike():
    nombre=libreria.pedir_nombre("ingrese nombre:")
    contenido=nombre + "\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print(" Se guardaron datos")
    print("")
def MarcaPuma():
    nombre=libreria.pedir_nombre("ingrese nombre:")
    contenido=nombre + "\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print(" Se guardaron datos")
    print("")
def Leerdatos_Marcas():
    marcas=libreria.obtener_datos("info.txt")
    if (marcas != ""):
        print(marcas)
    else:
        print("No contiene nada el archivo")
opc=0
max=5
while(opc!=max):
    print("####### Menu Marcas #####")
    print("1.Adidas                 ")
    print("2.Nike                   ")
    print("3.Puma                   ")
    print("4.leer datos")
    print("5.Salir                  ")

    opc=libreria.pedir_numero("ingrese opcion:",1,4)
    # Mapeo de las opciones
    if (opc==1):
        MarcaAdidas()
    if (opc==2):
        MarcaNike()
    if (opc==3):
        MarcaPuma()
    if (opc == 4):
        Leerdatos_Marcas()
    # fin_if
#fin_while
print("fin del programa ...........")
