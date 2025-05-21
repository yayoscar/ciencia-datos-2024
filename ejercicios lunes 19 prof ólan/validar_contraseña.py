def fuerza(contrsena):
    tiene_mayuscula = any(letra.isupper() for letra in contrasena)
   tiene_digito = any(letra.isdigit() for letra in contrasena)
   longitud_valida = len(contrasena) >= 8
   if tiene_mayuscula and tien_digito and lingitud_valida:
       return "Contraseña Fuerte"
   else:
       return "Contraseña Débil"
contrasena_usuario = input("Ingresa una contraseña: ")
print(fuerza(contrasena_usuario))
