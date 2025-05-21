def saludo_nom(nombre_local):
    saludo = f"Hola {nombre_local.capitalize()}"
    return saludo
nombre = input('Nombre: ')
print(saludo_nom(nombre))