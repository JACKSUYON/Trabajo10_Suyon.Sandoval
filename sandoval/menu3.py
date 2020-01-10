import libreria
# Menu calcular la distancia
def calcularDistancia():
    velocidad=libreria.pedir_num("ingrese velocidad:")
    tiempo=libreria.pedir_num("ingrese tiempo:")
    distancia=velocidad*tiempo
    contenido= str(velocidad) + "-" + str(tiempo) + " distacia es:" + str(distancia) + "\n"
    libreria.guardar_datos("info.txt",contenido, "a")
    print("se guardaro datos ")

def obtenerDistacia():
    distancia = libreria.obtener_datos("info.txt")
    if ( distancia !=""):
        print(distancia)
    else:
        print("archivo sin datos ")


opc=0
max=3
while(opc!=max):
    # calcular la distancia
    print("###### Menu #######")
    print("1.Calcular Distancia")
    print("2.Obtener Distancia")
    print("4.salir")

    opc=libreria.pedir_numero("ingrese opcion:",1,3)

    if (opc==1):
        calcularDistancia()
    if (opc==2):
       obtenerDistacia()
    #fin_if
# fin_while
print("fin del programa.............")
# fin_programa
