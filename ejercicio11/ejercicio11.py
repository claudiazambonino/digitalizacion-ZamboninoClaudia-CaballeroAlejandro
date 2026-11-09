### Escriba un programa que permita crear dos
#   listas de palabras (se pedirá cuantas palabras
#   se van a introducir en cada lista)  y que, a
#   continuación, elimine de la primera lista los
### nombres de la segunda lista.
# ALEJANDRO CABALLERO Y CLAUDIA ZAMBONINO

cont=0
cont2=0
lista1 = []
lista2 = []

palabras= int(input("Cuantas palabras quieres en la primera lista: "))
for i in range (palabras):
    cont = cont+1
    agregar = input(f"Introduce la cadena {cont}: ")
    lista1.append(agregar)

palabras2= int(input("Cuantas palabras quieres en la segunda lista: "))
for i in range (palabras2):
    cont2 = cont2+1
    agregar2 = input(f"Introduce la cadena {cont2}: ")
    lista2.append(agregar2)
    
for i in lista2:
    if i in lista1:
        lista1.remove(i)
        
print("Lista 1:", lista1)
print("Lista 2:", lista2)