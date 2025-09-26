"""
Ejercicio 3

Escribir un programa que pregunte el nombre del usuario en la consola y
después de que el usuario lo introduzca muestre por pantalla <NOMBRE>
tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.

entradas: nombre salidas: letras
tabla:
nombre      numero de letras
Daniel      tiene 6 letras
"""
def ejericicio():
    nm = input("ingrese el nombre\n")
    nms = nm.split(" ")
    s =0 
    for n in nms:
        s = len(n) + s
    print(nm.upper(), "tiene", s, "letras")