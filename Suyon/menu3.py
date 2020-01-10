import libreria
def volumenMultimedia():
    print("se activo el volumen de multimedia")
def volumenLLamada():
    print("se activo el volumen de llamada")
def volumenTono():
    print("se activo el volumen de tono ")
def volumenAlarma():
    print("se activo el volumen de alarma")

opc=0
max=5

while(opc!=max):
    print("### MENU DE SONIDO ###")
    print("1.Volumen multimedia")
    print("2.Volumen de llamada")
    print("3.Volumen de tono ")
    print("4.Volumen de alarma")
    print("5.Salir")
    print("#####################")

    opc=libreria.pedir_numero("active el volumen:",1,5)

    if(opc == 1):
        volumenMultimedia()
    if(opc == 2):
        volumenLLamada()
    if(opc == 3):
        volumenTono()
    if(opc == 4):
        volumenAlarma()
print("fin programa")
