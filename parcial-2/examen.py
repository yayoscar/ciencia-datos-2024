def validar_contrasena(contraseña):
    lon =len(contraseña) >= 8
    may = any(c.isupper() for c in contraseña)
    digit = any(d.isdigit() for d in contraseña)
    return lon and may and digit


with open("actividades.txt","r") as actividades_archivo:
    for usuario in actividades_archivo:
        partes = usuario.strip().split("|")
        nombre_usuario = partes[0]
        actividad_usuario = partes[1]
        duracion_usuario = partes[2]
        contrasena_usuario = partes[3]

        contrassena_funcion = "Fuerte" if validar_contrasena(contrasena_usuario) else "Debil"

        print(f"{nombre_usuario.capitalize()}: realizó {actividad_usuario} por {duracion_usuario} minutos - Contraseña: {contrassena_funcion}\n")