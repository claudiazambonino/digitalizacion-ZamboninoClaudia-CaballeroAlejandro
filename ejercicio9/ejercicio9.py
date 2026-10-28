dni= int(input("Introduce un DNI: "))
cadena="TRWAGMYFPDXBNJZSQVHLCKE"
modulo=dni % 23
letra = cadena[modulo]

print(letra)