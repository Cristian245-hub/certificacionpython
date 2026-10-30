matriz = [
    ['A', 'B', 'C', 'D', 'E'],
    ['F', 'G', 'H', 'I', 'J'],
    ['K', 'L', 'M', 'N', 'Ñ'],
    ['O', 'P', 'Q', 'R', 'S'],
    ['T', 'U', 'V', 'W', 'X'],
    ['Y', 'Z', ]
]

filas = 6
columnas = 2

for i in range(filas):
    for j in range(columnas):
        print(f"Posición [{i}][{j}] = {matriz[i][j]}")