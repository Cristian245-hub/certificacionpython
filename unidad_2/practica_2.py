inventario = {
    "lapiz": 10,
    "cuaderno": 5,
    "borrador": 8
}

producto = input("Solicita un producto: ").lower()
cantidad = int(input("Solicita la cantidad: "))

if producto in inventario:
    if cantidad > 0 and cantidad <= inventario[producto]:
        print("Venta autorizada")
        inventario[producto] = inventario[producto] - cantidad
        print("Existencia restante:", inventario[producto])
    else:
        print("Venta rechazada: cantidad no disponible")
else:
    print("Venta rechazada: el producto no existe")

print("Inventario final:", inventario)