import libreria
# Menu de calcular la fuerza
def CalcularFuerza():
    masa=libreria.pedir_num("ingrese masa:")
    aceleracion=libreria.pedir_num("ingrese aceleracion:")
    fuerza=masa*aceleracion
    contenido= str(masa) + "-" + str(aceleracion) + "-"+ "fueza es" + str(fuerza) + "\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print("SE GUARDARON DATOS")
def obtenerFuerza():
    fuerza= libreria.obtener_datos("info.txt")
    if (fuerza !=""):
        print(fuerza)
    else:
        print("NO CONTIENE DATOS")
    # fin_if
#fin_def
opc=0
max=3
while(opc!=max):
    # calcular la fuerza
    print("##### Menu #######")
    print("1.calcular Fuerza ")
    print("2.obtener fuerza  ")
    print("3.Salir           ")

    opc=libreria.pedir_numero("ingrese opcion:",1,4)

    if (opc==1):
        CalcularFuerza()
    if (opc==2):
        obtenerFuerza()

    # fin_if
# fin_while

print("fin del programa .........")
