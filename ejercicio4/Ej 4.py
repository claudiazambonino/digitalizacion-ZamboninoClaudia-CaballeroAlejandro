valor = int(input("Introduce un valor: "))
if valor % 2==0 and valor % 4 !=0:
    print("Es múltiplo de dos")
elif valor %2==1:
    print("No es múltiplo de 2")
elif valor % 2==0 and valor %4 ==0:
    print("Es múltiplo de dos y cuatro")