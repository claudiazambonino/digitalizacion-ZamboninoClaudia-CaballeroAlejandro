total_factura = 0
print("Calcular Factura (Introduce 0 para terminar)")
cantidad = int(input("Introduce la cantidad de unidades vendidas: "))

while cantidad != 0:
    while cantidad < 0:
        print("La cantidad debe ser un número positivo.")
        cantidad = int(input("Introduce la cantidad de unidades vendidas: "))
    if cantidad != 0:
        precio = float(input("Introduce el precio unitario: "))
        while precio <= 0:
            print("El precio debe ser un número mayor que 0.")
            precio = float(input("Introduce el precio unitario: "))
        
        total_factura = total_factura + (cantidad * precio)
        print("Artículo añadido correctamente.")
        
        cantidad = int(input("Introduce la cantidad de unidades vendidas: "))
print("Factura Final: ")
print("El importe total de la factura es:", round(total_factura,2))