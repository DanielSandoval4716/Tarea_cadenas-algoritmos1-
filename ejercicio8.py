"""
Ejercicio 8

Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y
muestre por pantalla el número de euros y el número de céntimos del precio introducido.
entradas: euros
salidas: euros_completos, centavos
tabla:
euros        euros_enteros      centavos
6.28        6                   28
"""

def ejercicio():
    pr = input("ingrese sus euros:\n")
    prs = pr.split(".")
    print(f"la cantidad de euros es: {prs[0]} y los centimos son: {prs[1]}")

ejercicio()