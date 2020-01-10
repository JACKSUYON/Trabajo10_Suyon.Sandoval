import libreria

opc=0
max=5

while(opc!=max):
    print("### MENU DE ORDENAR ###")
    print("1. Ordenar por Nombre")
    print("2. Ordenar por Tamaño")
    print("3. Ordenar por Tipo de elemento")
    print("4. Ordenar por Fecha de modificacion")
    print("5. Salir")

    opc=libreria.pedir_numero("Ingrese la opcion en que se desea Ordenar",1,5)


    if(opc==1):
        ordenarNombre()

    if(opc==2):
        ordenarTamaño()

    if(opc==3):
        ordenarTipoElemento()

    if(opc==4):
        ordenarFecharModificacion()

print("fin del programa")
