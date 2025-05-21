def largo(contrasena):
    largo = False
    carac = len(contrasena)
    mensaje = "no cumple con el largo"
    if carac >= 8:
        largo = True
        mensaje = "cumple con el largo"
    condiciones.append(largo)
    return mensaje

def mayus(contrasena):
    mayus = False
    mensaje = "no cumple con la mayuscula"
    for caracter in contrasena:
        if caracter.isupper():

         mayus = True
        mensaje = "cumple con la mayuscula"
    condiciones.append(mayus)

    return mensaje
def num(contrasena):
    num = False
    mensaje = "no cumple con el numero"
    for carac in contrasena:
        if carac.isdigit():
            num = True
            mensaje = "cumple con el numero"
        condiciones.append(num)

    return mensaje

condiciones = []
contrasena=input("ingresa tu contraseña: ")
print(largo(contrasena))
print(mayus(contrasena))
print(num(contrasena))

if all(condiciones):
    print("contraseña segura")
else:
    print("contraseña debil")