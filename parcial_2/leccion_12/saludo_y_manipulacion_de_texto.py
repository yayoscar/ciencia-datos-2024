def saludo_capitalizado():
    saludo = "hola "
    nombre = input("ingrese su nombre: ")
    saludo2 = saludo + nombre
    saludo2 = saludo2.title()
    return saludo2

print(saludo_capitalizado())