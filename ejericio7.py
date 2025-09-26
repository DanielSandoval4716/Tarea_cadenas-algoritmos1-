"""
Ejercicio 7

Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre
por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es
entradas: correo electronico
salida: correo_con_ceu.es

tabla:
correo                  correo_modificado
46716@gmail.com         4716@ceu.es
"""
def ejercicio():
    email = input("Introduce tu correo electrónico: ")
    nombre = email.split('@')
    print(f"{nombre[0]}@ceu.es")

ejercicio()