import libreria
def politica():
    print("elegida")
    print("elegida")
    contenido="se eligio la opcion noticias de tipo politica \n"
    libreria.guardar_datos("texto.txt",contenido,"a")
    print("se guradron los datos...")
def deporte():
    print("elegida")
    contenido="se eligio la opcion noticias de tipo deporte \n"
    libreria.guardar_datos("texto.txt",contenido,"a")
    print("se guradron los datos...")
def espectaculo():
    print("elegida")
    contenido="se eligio la opcion noticias de tipo espectaculo \n"
    libreria.guardar_datos("texto.txt",contenido,"a")
    print("se guradron los datos...")


def noticia():
    opc=0
    max=4
    while(opc!=max):
        print("#### NOTICIAS ####")
        print("1.Politica")
        print("2.Deporte")
        print("3.Espectaculo")
        print("4.salir")
        print("#################")

        opc=libreria.pedir_numero("ingrese el tipo de noticia que quiere ver :",1,4)

        if(opc==1):
            politica()

        if(opc==2):
            deporte()

        if(opc==3):
            espectaculo()

def musica():
    print("se ingreso a musica")

def videos():
    print("se ingreso a video")



opc=0
max=4

while(opc!=max):
    print("#### MENU DE HERRAMIENTAS ###")
    print("#1. Noticias ")
    print("#2. Musica ")
    print("#3. Videos ")
    print("#4. Salir")
    print("#############################")

    opc=libreria.pedir_numero("ingrese la opcion:",1,4)

    if (opc==1):
        noticia()
    if (opc==2):
        musica()
    if (opc==3):
        videos()

print("fin programa")
