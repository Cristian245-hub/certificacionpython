promedio=[9, 10, 16, 5, 7]
#1.Encontrar el rpomedio mas bajo usando un ciclo for
#suponemos inicialmente que el promedio mas bajo es el primer elemnto
promedio_bajo = promedio[0]
for contador in promedio:
    if contador < promedio_bajo:
        promedio_bajo = contador

promedio_alto = promedio[0]
for contador in promedio:
    if contador > promedio_alto:
        promedio_alto = contador
print("Promedio bajo:", promedio_bajo)
print("Promedio alto:", promedio_alto)












