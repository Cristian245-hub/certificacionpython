#Cadenas  y concatenacion con (+)
cadena1= 'Hola'
cadena2="Mundo"
multilinea="""Estos es una cadena
de varias lineas"""
print(cadena1 + cadena2 + multilinea)
#Cadena y repeticion
eco="ja"*3
print(eco)
#Cambiar una cadena de minuscula a mayuscula
tu_nombre='Alex'
print(tu_nombre.upper())
#Cambiar una cadena de mayuscula a minuscula
print(tu_nombre.lower())
#Remplazar texto en una cadena
frase="Me gusta programacion"
print(frase.replace("programacion","matematicas"))
#Formato de concatenar cadenas  con valores (F-String)
edad=16
Nombre='Alex'
mensaje=f"Hola, me llamo  {Nombre} y tengo\n{edad}años"
print(mensaje)
#Contar las caracteres de una cadena
texto= "¡Felicidades por aun continuar en el CECY!!!"
cantidad_caracteres=len(texto)
print(cantidad_caracteres)
#Comprar si un texto contiene una palabra
oracion="Aprender python es divertido"
if "python" in oracion:
    print("Encontrado")
else:
    print("No esta")
#Validar contenido de una cadena
ncadena="a1"
print(ncadena.isalpha())#True
print(ncadena.isdigit())#False