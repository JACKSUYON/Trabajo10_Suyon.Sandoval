import libreria
def juegos():
    print("ingreso a Juegos")
def apps():
    print("ingreso a Apps")
def peliculas():
    print("ingreso a Peliculas")
def libros():
    print("ingreso a Libros")

opc=0
max=5

while(opc!=max):
    print("###MENU DE PLAY STORE ####")
    print("1. Juegos")
    print("2. Apps")
    print("3. Peliculas")
    print("4. Libros")
    print("5. Salir")
    print("#############")

    opc=libreria.pedir_numero("Ingrese la opcion de PLAY STORE:",1,5)


    if(opc == 1):
        juegos()

    if(opc == 2):
        apps()

    if(opc == 3):
        peliculas()

    if(opc == 4):
        libros()

print("fin del programa")
