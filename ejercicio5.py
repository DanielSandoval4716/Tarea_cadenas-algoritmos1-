"""
Ejercicio 5

Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.
entradas; frase
salida = frase_invertida

tabla:
frase       salida
"Hola mundo"    "odnum aloH"
"""

def ejericicio():
    fr = input("ingrese la frase:\n")
    for i in range(len(fr),0,-1):
        print(fr[i-1], end="")

ejericicio()