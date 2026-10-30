#El mapa del tesoro
mapa=[
    [".",".",".","."],
    [".","Y",".","."],
    [".",".",".","A"],
    [".",".",".","."]
]
filas=len(mapa)
columnas=len(mapa[0])
#Recorriendo la matriz con ciclos anidades
#ciclo externo para manejas columnas(i)
for i in range(filas):#i<4
    #ciclo externo para manejas columnas(j)
    for j in range(columnas):
     if mapa[i][j]=="A":#[0][0]==x
      print(f"Tesoro encontrado en la posicion [{i}][{j}]")
     if mapa[i][j]=="Y":#[0][0]==x
          #[0][1]==x
        print(f"Tesoro encontrado en la posicion [{i}][{j}]")
    