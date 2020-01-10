import libreria

def notificacionMes():
    print("se eligio la notificacion de hace un mes")

def notificacionSemana():
    print("se eligio la notificacion de hace un Semana")

def notificacionDia():
    print("se eligio la notificacion de hace un Dia")

opc=0
max=4

while ( opc != max ):
    print("### MENU DE NOTIFICACIONES ####")
    print("1.Notificaciones hace un mes")
    print("2.Notificaciones hace una semana")
    print("3.Notificaciones hace un dia")
    print("4.Salir de notificaciones")
    print("###############################")

    opc=libreria.pedir_numero("elegir la opcion:",1,4)

    if(opc == 1):
        notificacionMes()

    if(opc == 2):
        notificacionSemana()

    if(opc == 3):
        notificacionDia()

print("fin de programa")
