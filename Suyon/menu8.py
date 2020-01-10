import libreria

def paseoPircas():
    print("se eligio el paseo a Pircas")

def paseoAguaPark():
    print("se eligio el paseo a AguaPark")

def paseoMirador():
    print("se eligio el paseo al Mirador")


opc=0
max=4


while( opc != max ):
    print("### MENU ###########")
    print("1.Paseo a las Pircas")
    print("2.Paseo a AguaPark")
    print("3.paseo al Mirador")
    print("4.salir")
    print("###################")

    opc=libreria.pedir_numero("ingrese el lugar de recreacion:",1,4)

    if(opc == 1):
        paseoPircas()

    if(opc == 2):
        paseoAguaPark()

    if(opc ==3):
        paseoMirador()

print("fin del programa")
