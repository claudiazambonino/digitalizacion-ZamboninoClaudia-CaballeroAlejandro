user_correcto = "root"
clave_correcta = "1234"

usuario = input("Introduce el nombre de usuario: ")
clave = input("Introduce la contraseña: ")
intentos = 1

while (usuario != user_correcto or clave != clave_correcta) and intentos < 3:
    print("Datos incorrectos.")
    print("Intentos restantes:", 3 - intentos)
    usuario = input("Introduce el nombre de usuario: ")
    clave = input("Introduce la contraseña: ")
    intentos = intentos + 1
if usuario == user_correcto and clave == clave_correcta:
    print("¡Bienvenido al sistema!")
else:
    print("Lo sentimos, se ha superado el número de intentos permitido.")