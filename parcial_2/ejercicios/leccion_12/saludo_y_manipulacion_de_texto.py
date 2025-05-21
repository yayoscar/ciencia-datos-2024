def saludo_capitalize(nombre):
    saludo = 'Hola ' + nombre.capitalize()
    return saludo
nombre = input("Escribe tu nombre: ")
print(saludo_capitalize(nombre))