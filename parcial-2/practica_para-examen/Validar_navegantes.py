def validar_contrasena(contrasena):
    lon = len(contrasena) >=8
    mayu = any(c.isupper() for c in contrasena)
    digito = any(c.isdigit() for c in contrasena)
    return lon and mayu and digito

def validar_correo(correos):
    if "@" in correos:
        return True
    return False

with open("Navegantes.txt","r") as archivo_principal, open("navegantes_validados.txt","w") as navegantes_actualizado:
    for navegantes in archivo_principal:
        partes = navegantes.strip().split("|")
        nombre_usuario = partes[0]
        correo_usuario = partes[1]
        contrasena_usuario =partes[2]

        contrasena_funcion = "fuerte" if validar_contrasena(contrasena_usuario) else "debil"
        correo_funcion = "valido" if validar_correo(correo_usuario) else "invalido"

        navegantes_actualizado.write(f"Nombre: {nombre_usuario} - Correo: {correo_usuario} validez: {correo_funcion} contraseña:{contrasena_funcion}\n")
