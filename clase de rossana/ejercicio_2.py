def validar_contrasena(contrasena):
    if len(contrasena) < 8:
        return False,"La contraseña debe tener minimo 8 caracteres"
    tiene_mayuscula = any(caracter.isupper() for caracter in contrasena)
    if not tiene_mayuscula:
        return False, "La contraseña debe tener almenos una mayuscula"
    tiene_numero = any(caracter.isdigit()for caracter in contrasena)
    if not tiene_numero:
        return False, "la contraseña debe tener almenos un numero."
    return True, " la contraseña es segura."

def main():
    contrasena = input("ingrese una contraseña:")
    es_segura, mensaje = validar_contrasena(contrasena)
    print(mensaje)
    if not es_segura:
        print ("porfavor intente de nuevo con una contraseña mas segura")
if __name__ == "__main__":
    main()





