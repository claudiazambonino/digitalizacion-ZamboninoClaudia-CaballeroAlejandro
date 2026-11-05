### Escriba un programa que permita crear una
#   lista de palabras (se pedirán palabras hasta
#   que se meta un espacio) y que, a continuación,
#   pida dos palabras y sustituya la primera por la
### segunda en la lista.
lista = []
salir=input("Introduce palabras a la lista: ")

while salir!=" ":
    lista.append(salir)
    salir=input("Introduce palabras a la lista: ")
    
palabra1 = input("Introduce una palabra")
palabra2 = input("Introduce la palabra a sustituir")
for i in range(len(lista)):
    if lista[i]==palabra1:
        lista[i]=palabra2
print(lista)