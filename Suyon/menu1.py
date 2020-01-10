import libreria

def noticia():
    print("se ingreso a noticias")
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
