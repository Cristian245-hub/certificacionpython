
#Creando un diccionario en python
persona={
    "nombre":"sofia",
    "edad":28,
    "profesion":"Ingenieria",
    "estudiante":False
}
print(persona)
#Accediendo un valor especifico
print(persona["profesion"])
#Se puede usar el metodo .get()
#Es util porque no da error si la clave no existe
print(persona.get("edad"))
#Modificar un valor existente
persona["edad"]=29
print(persona.get("edad"))
#Agregar un par(clave:valor)
persona["ciuddad"]="San pepe ranch"
print(persona)
#Recorrer un diccionario con un bucle
for clave,valor in persona.items():
    print(f"{clave}:{valor}")