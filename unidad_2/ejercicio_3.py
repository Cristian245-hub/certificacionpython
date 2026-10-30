colores=["azul","morado","rojo","amarrillo","verde"]
color=input("Ingresa el color:")#naranja
encontrado=False
for contador in colores:
    print(contador)
    #Si el clor actual es "Rojo",detener el bucle
    if contador==color:
        print("color encontrado! saliendo del bucle")
        encontrado=True
        break
if  not encontrado :
        print("El color,",color, "no se encontro")    
    