alumnos = ["Cristian", "Estrella", "Santa", "Yovani",
           "Jenny", "Mayte", "Michel", "Yael"]

promedio = []

for nombre in alumnos:
    calificacion = float(input("Ingresa el promedio de " + nombre + ": "))
    promedio.append(calificacion)

promedio_alto = promedio[0]
promedio_bajo = promedio[0]
alumno_alto = alumnos[0]
alumno_bajo = alumnos[0]

print("\n--- PROMEDIO DE CADA ALUMNO ---")

for i in range(8):
    print(alumnos[i], ":", promedio[i])

    if promedio[i] > promedio_alto:
        promedio_alto = promedio[i]
        alumno_alto = alumnos[i]

    if promedio[i] < promedio_bajo:
        promedio_bajo = promedio[i]
        alumno_bajo = alumnos[i]

print("\nPromedio mas alto:", alumno_alto, promedio_alto)
print("Promedio mas bajo:", alumno_bajo, promedio_bajo)