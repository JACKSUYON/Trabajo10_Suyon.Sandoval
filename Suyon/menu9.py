import libreria

def generos():
    print("se eligio la opcion Generos")

def artistas():
    print("se eligio la opcion Artistas")

def albunes():
    print("se eligio la opcion albunes")

opc=0
max=4

while ( opc != max ):
    print("### PLAY LIST ###")
    print("1. Generos")
    print("2. Artistas")
    print("3. Albunes")
    print("4. Salir")
    print("#################")


    opc=libreria.pedir_numero("ingrese la opcion(PLAY LIST) :",1,4)


    if (opc==1):
        generos()

    if (opc==2):
        artistas()

    if (opc==3):
        albunes()

print("fin del programa ")
