"""
Ejercicio 6

Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal,
y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.
entradas: frase, vocal
salida: frase_reemplazada_con_vocal

tabla:
frase       vocal       salida
"Hola mundo"      a           "AAAA AAAAA"
"""

def ejercicio():
    fr = input("ingrese la frase\n")
    v = input("ingrese la vocal\n")
    for c in fr:
        if c != " ":
            print(v.upper(), end="")
        else:
            print(" ", end="")

ejercicio()