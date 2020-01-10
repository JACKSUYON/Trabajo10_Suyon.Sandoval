import libreria
def platanos():
    nro=libreria.pedir_numero("ingrese la cantidad:",1,100)

def uvas():
    nro=libreria.pedir_numero("ingrese la cantidad:",1,100)

def manzana():
    nro=libreria.pedir_numero("ingrese la cantidad:",1,100)



def frutas():
    print("se eligio la opcion Frutas")
    opc=0
    max=4
    while(opc!=max):
        print("##Frutas##")
        print("#1.Platano")
        print("#2.Uvas")
        print("#3.manzanas")
        print("#4.Salir")
        print("#########")

        opc=libreria.pedir_numero("ingrese el tipo de frutas:",1,4)


        if( opc == 1):
            platanos()
        if( opc == 2):
            uvas()
        if( opc == 3):
            manzana()




def verduras():
    print("se eligio la opcion Verduras")

opc=0
max=3

while(opc!=3):
    print("### MENU ###")
    print("#1. Frutas ")
    print("#2. Verduras")
    print("#3. salir")
    print("###########")

    opc=libreria.pedir_numero("ingrese la opcion:",1,3)

    if( opc == 1):
        frutas()
    if( opc == 2):
        verduras()

print("fin del menu")
