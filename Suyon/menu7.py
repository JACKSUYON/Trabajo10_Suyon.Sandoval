import libreria
def configuracion():
    print("se accedio a la configuracion")

def idioma():
    print("se accedio a idioma")


opc=0
max=3

while( opc != max ):
    print("## MENU ##")
    print("1.Configuracion")
    print("2.Idioma")
    print("3.salir")

    opc=libreria.pedir_numero("eliga la opcion:",1,3)

    if( opc == 1 ):
        configuracion()

    if( opc == 2 ):
        idioma()


    print("fin del programa ")
