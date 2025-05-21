def saludo(nombre_persona):
    saludo = f"Hola {nombre_persona.capitalize()}"
    return saludo

nombre_persona = input("ingrese su nombre: ")
print(saludo(nombre_persona))