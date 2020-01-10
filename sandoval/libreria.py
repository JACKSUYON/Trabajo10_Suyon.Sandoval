def validar_numero(nmr):
    if (isinstance(nmr,int)):
        return True
    else:
        return False


def validar_rango(n,ri,rf):
    if ( validar_numero(n)==True):
        if (n>=ri and n<=rf):
            return True
        else:
            return False
    else:
        return False

def pedir_numero(nr,ri,rf):
    n=""
    while(validar_rango(n,ri,rf)==False):
        n=input(nr)
        if(n.isdigit()==True):
            n=int(n)
    return n


def validar_nombre(nombre):
    if (isinstance(nombre,str)):
        if (len(nombre)>=3):
            return True
        else:
            return False
    else:
        return False
def pedir_nombre(msg):
    nombre=""
    while (validar_nombre(nombre)==False):
        nombre=input(msg)
    # fin_while
    return nombre
# fin_pedir_nombre

def validar_cargo(ocupacion):
    if (isinstance(ocupacion,str)):
        if (len(ocupacion)>=6):
            return True
        else:
            return False
    else:
        return False

def pedir_ocupacion(msg):
    ocupacion=""
    while (validar_cargo(ocupacion)==False):
        ocupacion=input(msg)
    #fin_while
    return ocupacion


def validar_entero_positivo(n):
    if(isinstance(n,int)):
        if (n>0):
            return True
        else:
            return False
    else:
        return False

def pedir_num(msg):
    n=-1
    while(validar_entero_positivo(n) == False):
        n = int(input(msg))
    #fin_while
    return n


def guardar_datos(nombre_archivo,contenido,modo):
    archivo=open(nombre_archivo,modo)
    archivo.write(contenido)
    archivo.close()

def obtener_datos(nombre_archivo):
    archivo=open(nombre_archivo)
    contenido=archivo.read()
    return contenido




