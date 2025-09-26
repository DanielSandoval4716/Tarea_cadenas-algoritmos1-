"""

Ejercicio 10

Escribir un programa que pregunte por consola por los productos de una cesta de la compra,
separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.
entradas: lista_de_articulos
salida: articulos_por_linea
tabla:
lista                           salida
ropa,jabon,reloj                ropa
                                jabon
                                reloj
"""

def ejercicio():
    cs = input("ingrese la cesta separada por comas:\n")
    cs = cs.split(",")
    for c in cs:
        print(c)

ejercicio()