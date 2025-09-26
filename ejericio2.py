"""
Ejercicio 2

Escribir un programa que pregunte el nombre completo del usuario en la consola y 
después muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, 
otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula.
El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.

entradas: nombre_completo
salida: nombre_minuscula, nombre_mayuscula, nombre_title

tabla:
nombre:
Daniel Estuardo Sandoval Torres
print:
DANIEL ESTUARDO SANDOVAL TORRES
daniel estuardo sadoval torres
Daniel Estuardo Sandoval Torres
"""
def ejercicio():
    nm = input("ingrese su nombre completo\n")
    print(nm.upper())
    print(nm.lower())
    print(nm.title())


ejercicio()