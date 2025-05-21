def validar_contraseña(contraseña):
    if (len(contraseña) >= 8 and
            any(c.isupper() for c in contraseña) and
            any(c.isdigit() for c in contraseña)):
        return "Fuerte"
    return "Débil"


def formatear_linea(lineas_str):
    lineas = [(linea) for linea in lineas_str.split(',')]
    return lineas


with open("actividades.txt", "r") as archivo_local:
    lineas = archivo_local.readlines()

    for linea in lineas:
        nombre, act, tiempo = formatear_linea(lineas_str)
        seguridad = validar_contraseña()
        outpot = print(f"Nombre: {nombre}, realizó: {act}, Duración: {tiempo}, Contraseña: {seguridad}")