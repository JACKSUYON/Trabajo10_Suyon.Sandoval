import libreria

def frutas():
    print("se eligio la opcion Frutas")

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
