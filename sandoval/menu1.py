import libreria
# Menu de comida
def Ceviche():
    nombre=libreria.pedir_nombre("ingrese nombre pedido(ceviche,carne seca):")
    cantidad=libreria.pedir_num("ingrese nro de platos de:")
    costo=libreria.pedir_numero("ingrese costo:",1,50)
    contenido= nombre + "-" + str(cantidad) + "-" + str(costo) + "\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print("se guardaron datos")

def CarneSeca():
    nombre=libreria.pedir_nombre("ingrese nombre pedido(ceviche,carne seca):")
    cantidad=libreria.pedir_num("ingrese nro de platos de carne seca:")
    costo=libreria.pedir_numero("ingrese costo:",1,50)
    contenido= nombre + "-" + str(cantidad) + "-" + str(costo) + "\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print("se guardaron datos")



opc=0
max=3
while(opc != max):
    print("######## MENU ######")
    print("1.Ceviche           ")
    print("2.Carne Seca        ")
    print("3. Salir            ")

    opc=libreria.pedir_numero("ingrese opcion:",1,4)


    if (opc==1):
        Ceviche()
    if (opc==2):
        CarneSeca()

    # fin_if
#fin_while

print("Fin del programa...........")
