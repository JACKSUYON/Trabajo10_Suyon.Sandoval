import libreria

assert(libreria.validar_entero("a") == False)
assert(libreria.validar_entero("1") == False)
assert(libreria.validar_entero(10) == True)
print("validar_entero OK")

assert (libreria.validar_rango("a", 1, 5) == False)
assert (libreria.validar_rango(0, 1, 5) == False)
assert (libreria.validar_rango(1, 1, 5) == True)
assert (libreria.validar_rango(5, 1, 5) == True)
assert (libreria.validar_rango(6, 1, 5) == False)
print("validar_rango ok")

assert (libreria.validar_nombre("a") == False)
assert (libreria.validar_nombre("ab") == False)
assert (libreria.validar_nombre("ana") == True)
print("validar_nombre OK")

opc=libreria.pedir_numero("Ingrese num:", 1, 3)
assert (libreria.validar_rango(opc, 1, 3) == True)
print("pedir_numero OK")

