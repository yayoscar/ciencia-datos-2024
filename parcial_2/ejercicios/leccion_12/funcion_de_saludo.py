def saludo(nombre):
    saludo = 'Hola ' + nombre.capitalize()
    return saludo
nombre = input("Escribe tu nombre: ")
print(saludo(nombre))