def verificar_correo (correo):
    if "@" in correo:
        dominio = correo.split("@")[1]
        if "." in dominio:
            return True
    return False

def clasificar_estado(intentos):
    if intentos == 0:
        return "activo"
    elif 1 <= intentos <=3:
        return "Advertencia"
    else:
        return "bloqueada"



with open("usuarios.txt","r") as usuarios, open("usuarios_verificados.txt", "w") as usuarios_verificados:
    for usuario in usuarios:
        partes = usuario.strip().split("|")
        nombres = partes[0]
        correos = partes[1]
        intentos_usuario_str = partes[2]
        intentos_usuario = float(intentos_usuario_str)

        usuarios_verificados.write(f"Nombre: {nombres} - Correo:  {'valido' if verificar_correo(correos) else 'invalido'} - Estado: {clasificar_estado(intentos_usuario)}\n")

