import libreria
# Menu de un trabajador
def AgregarTrabajador():
    nombre=libreria.pedir_nombre("ingrese nombre:")
    cargo=libreria.pedir_ocupacion("ingrese ocupacion:")
    sueldo=libreria.pedir_num("ingrese sueldo:")
    contenido= nombre + "-" + cargo +  "-" + str(sueldo) + "\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print("datos guardados")

def LeerTrabajador():
    trabajador = libreria.obtener_datos("info.txt")
    if (trabajador !=""):
        print(trabajador)
    else:
        print("no se agregaron datos ")

    # fin_if

opc=0
max=3
while(opc!=max):
    # Leer el nombre,cargo,sueldo de un trabajador
    print("###### Menu #######  ")
    print("1.Nombre,cargo,sueldo")
    print("2.Leer Trabajador    ")
    print("3.Salir              ")

    opc=libreria.pedir_numero("ingrese opcion:",1,4)

    if (opc==1):
       AgregarTrabajador()

    if (opc==4):
        LeerTrabajador()

    #fin_if
# fin_while
print("fin del programa ........")
