cantidad_numeros = 0
suma_total = 0
print("Introduce números (el programa terminará al llegar a 10 num o suma de 100): ")

while cantidad_numeros < 10 and suma_total <= 100:
    numero = int(input("Introduce un número: "))
    cantidad_numeros = cantidad_numeros + 1
    suma_total = suma_total + numero
if suma_total > 100:
    print("Condición cumplida: La suma de los números es mayor que 100.")
else:
    print("Condición cumplida: Se han introducido 10 números.")