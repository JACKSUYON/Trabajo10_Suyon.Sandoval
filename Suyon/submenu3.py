import libreria



def volumen1():

    print("se guradron los datos...")
def volumen2():
    print("se guradron los datos...")
def volumen3():
    print("se guradron los datos...")




def volumenMultimedia():
        print("se activo el volumen de multimedia")
        opc=0
        max=4
        while(opc!=max):
            print("#### VOLUMRN DE MULTIMEDIA ####")
            print("1.VOLUMEN 1")
            print("2.VOLUMEN 2")
            print("3.VOLUMEN 3")
            print("4.salir")
            print("#################")

        opc=libreria.pedir_numero("ingrese el tipo de noticia que quiere ver :",1,4)

        if(opc==1):
            volumen1()

        if(opc==2):
            volumen2()

        if(opc==3):
            volumen3()




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
