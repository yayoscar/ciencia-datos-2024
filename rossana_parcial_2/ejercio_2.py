import re

def es_contraseña_segura(contraseña):
    if len(contraseña) < 8:
        print(" La contraseña debe tener al menos 8 caracteres.")
        return False
    if not re.search(r"[A-Z]", contraseña):
        print(" Debe contener al menos una letra mayúscula.")
        return False
    if not re.search(r"[a-z]", contraseña):
        print(" Debe contener al menos una letra minúscula.")
        return False
    if not re.search(r"[0-9]", contraseña):
        print(" Debe contener al menos un número.")
        return False
    if not re.search(r"[!@#$%^&*()_+=\-{}[\]:;\"'<>,.?/]", contraseña):
        print(" Debe contener al menos un símbolo.")
        return False
    return True

# Pedir al usuario que cree su propia contraseña
while True:
    contraseña_usuario = input("Crea una contraseña segura: ")
    if es_contraseña_segura(contraseña_usuario):
        print("¡Contraseña segura creada exitosamente!")
        break
    else:
        print("Intenta nuevamente.\n")

