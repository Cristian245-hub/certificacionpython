#creando una matriz
matriz=[
    [5,8,1],#fila 1 x 3 columnas
    [3,9,2]#fila2 2 x 3 colimnas
]
#obteniendo el numero total de las filas y columnas
filas=len(matriz)
columnas=len(matriz[0])
#ciclo externo para los indices de las filas(i)
for i in range(0,2):
    #ciclo externo para los indices de las columnas
    for j in range(0,3):
        print(f"Posicion[{i}][{j}]={matriz[i][j]}")