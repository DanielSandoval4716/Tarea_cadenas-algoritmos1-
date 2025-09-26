"""
Ejercicio 4

Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde 
el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56).
Escribir un programa que pregunte por un 
número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión

entradas: numero_de_telefono
salidas: numero_sin_prefijo
tabla:
    numero      salida
+34-59494312-56     59494312
"""

def ejercicio():
    n = input("ingrese su numero de telefono\n")
    ns = n.split("-")
    print(ns[1])

ejercicio()