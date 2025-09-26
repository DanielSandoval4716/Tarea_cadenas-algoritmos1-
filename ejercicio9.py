"""
Ejercicio 9

Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y
muestra por pantalla, el día, el mes y el año.
Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.
entradas: fecha
salida: dia,mes,año
tabla:
fecha       dia     mes     año
27/05/2025  27      5       2025
"""

def ejercicio():
    fe = input("Ingresa tu fecha de nacimiento en formato dd/mm/aaaa: ")
    fe =fe .split("/")
    print(f"Dia: {fe [0]}")
    print(f"Mes: {fe [1]}")
    print(f"Año: {fe [2]}")
ejercicio()