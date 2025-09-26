import sys
"""
Ejercicio 1

Escribir un programa que pregunte el nombre del usuario en la consola y 
un número entero e imprima por pantalla en líneas distintas el nombre del usuario 
tantas veces como el número introducido

entradas: nombre y numero
salida: nombre repetido

tabla:
nombre  numero
Daniel  3
salidas
Daniel
Daniel
Daniel
"""

#if len(sys.argv) == 3:
    #for i in range(0,int(sys.argv[2])):
        #print(sys.argv[1])
#else:
    #print("no se ingresaron los datos correctamente(un nombre, un numero)")
def ejercicio():
    dts = input("ingrese los datos (nombre y numero)\n")
    dts = dts.split(" ")
    if len(dts) == 2:
        for i in range(0,int(dts[1])):
            print(dts[0])
    else:
        print("no se ingresaron los datos correctamente(un nombre, un numero)")

ejercicio()