import libreria
# Menu de calcular Area de trapecio
def CalcularArea():
    base1=libreria.pedir_num("ingrese base 1:")
    base2=libreria.pedir_num("ingrese base 2:")
    altura=libreria.pedir_num("ingrese altura:")
    area_trapecio=(base1+base2)/2*altura
    contenido=str(base1) +"-" + str(base2) + "-" + str(altura) + "araea_trapecio" + str(area_trapecio) + "\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print("GUARDARON DATOS")
def obtenerArea():
    area_trapecio=libreria.obtener_datos("info.txt")
    if (area_trapecio != ""):
        print(area_trapecio)
    else:
        print("NO SE ENCONTRARON DATOS ")
opc=0
max=3
while(opc!=max):
    # calcular area del trapecio
    print("############################")
    print("###### Menu ################")
    print("1.calcular Area del trapecio")
    print("2.obtener Area              ")
    print("3.salir                     ")
    print("###########FIN##############")

    opc=libreria.pedir_numero("ingrese numero:",1,5)

    if (opc==1):
        CalcularArea()
    if (opc==2):
        obtenerArea()
    # fin_if
#fin_while
print("fin de programa ..........")
