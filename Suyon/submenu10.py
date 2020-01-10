import libreria

def reservarMañana():
    print("se reservo su cancha en el turno de mañana")
def reservarTarde():
    print("se reservo su cancha en turno Tarde")
def reservarNoche():
    print("se reservo su cancha en turno Noche")

opc=0
max=4

while( opc != max ):
    print("### RESERVAR CANCHA DEPORTIVA ###")
    print("1.Reservar cancha en la mañana")
    print("2.Reservar cancha en la tarde")
    print("3.Reservar cancha en la noche")
    print("4.Salir")
    print("#################################")


    opc=libreria.pedir_numero("ingrese la opcion para reservar cancha deportiva :",1,4)

    if( opc ==1):
        reservarMañana()
    if( opc ==2):
        reservarTarde()
    if( opc ==3):
        reservarNoche()
print("FIN DEL PROGRAMA")
