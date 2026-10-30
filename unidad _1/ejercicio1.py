precio1 = str(input("Introduce el precio del primer artículo: "))
precio2 = str(input("Introduce el precio del segundo artículo: "))
precio3 = str(input("Introduce el precio del tercer artículo: "))

nombre = str(input("Introduce el nombre del cliente: "))

total = float(precio1) + float(precio2) + float(precio3)
total = str(total)

print("Cliente: " + nombre)
print("Total de la compra:" + total)