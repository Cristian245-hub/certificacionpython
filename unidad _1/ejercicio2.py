try:
    alumnos= ["Cristian", "Estrella", "Santa", "yovani", "Jenny", "Michel","Mayte", "isabel","Yael"]
    calificaciones= [10, 9, 8, 7, 6, 5]
    print(alumnos[0])
    print(calificaciones[0])

    print(alumnos[2])
    print(calificaciones[2])
    
    print(alumnos[4])
    print(calificaciones[4])
except IndexError:
    print("index incorrecto")