def leer(archivo='actividades.txt'):
    with open(archivo,'r') as formato :
        todo = formato.readlines()
    return todo

def fuerza(contraseña):
    condiciones : []
    if len(contraseña) >=8 :
        condiciones.append(True)
    else:
        condiciones.append(False)

    digito = False
    for letra in contraseña:
        if letra.isdigit():
            digito = True

    condiciones.append(digito)

    mayuscula = False
    for letra in contraseña:
        if letra.isupper():
            mayuscula = True

    condiciones.append(mayuscula)

    if all(condiciones):
        return ("Password Fuerte")
    else:
        return ("Password debil")

def formatear_linea(archivo):
    separar = archivo.split('|')
    return separar

print(fuerza("Nologre"))