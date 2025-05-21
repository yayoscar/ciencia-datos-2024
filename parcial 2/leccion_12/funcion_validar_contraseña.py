import re
def evaluar_contrasena(contrasena):
    errores = []
    if len(contrasena) < 8:
        errores.append("La contrasena debe tener al menos 8 caracteres")
    if not re.search("[a-z]",contrasena) or not re.search("[A-Z]", contrasena):
        errores.append("La contrasena debe de tener letras mayusculas y minusculas")
    if not re.search("[0-9]", contrasena):
        errores.append("La contrasena debe de tener al menos 1 numero")
    if errores:
        return False, errores
    else:
        return True, "La contrasena es segura"
contrasena = input("Escriba la contrasena a evaluar:  ")
es_segura, mensaje = evaluar_contrasena(contrasena)
if es_segura:
    print(mensaje)
else:
    print("La contrasena no es segura:")
    for error in mensaje:
        print(error)

