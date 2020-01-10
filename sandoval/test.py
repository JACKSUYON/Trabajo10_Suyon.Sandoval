import libreria

assert (libreria.validar_numero("hola")==False)
assert (libreria.validar_numero(13456)==True)
assert (libreria.validar_numero(1)==True)
assert (libreria.validar_numero("jose")==False)
print("validar_numero ok")

assert (libreria.validar_rango(4,1,4)==True)
assert (libreria.validar_rango(0,1,4)==False)
assert (libreria.validar_rango(5,1,5)==True)
assert (libreria.validar_rango(3,4,5)==False)
assert (libreria.validar_rango(1,6,7)==False)
print("validar_rango OK")

assert (libreria.validar_nombre("jose")==True)
assert (libreria.validar_nombre("Elmer")==True)
assert (libreria.validar_nombre(12)==False)
assert (libreria.validar_nombre("3")==False)
print("valdar nombre ok")

assert (libreria.validar_cargo("obrero")==True)
assert  (libreria.validar_cargo("Estudiante")==True)
assert (libreria.validar_cargo("12345")==False)
assert (libreria.validar_cargo("ABCDE")==False)
assert (libreria.validar_cargo(12345)==False)
print("validar_cargo OK")


assert (libreria.validar_entero_positivo(2)==True)
assert (libreria.validar_entero_positivo(234)==True)
assert (libreria.validar_entero_positivo("HOLA")==False)
assert (libreria.validar_entero_positivo(234)==True)
assert (libreria.validar_entero_positivo(2.56)==False)
print("validar entero positivio ok")
