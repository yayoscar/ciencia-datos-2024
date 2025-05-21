
def validar_contrasena(contrasena):
    if (len(contrasena) >= 8 and
        any(c.isupper() for c in contrasena) and
        any(c.isdigit() for c in contrasena)):
        return "Fuerte"
    return "Débil"

with open("actividades.txt.txt", "r") as actividades:
    lineas = actividades.readlines()

with open("actividades.txt.txt", "w") as salida:
    for linea in lineas:
        try:
            usuario, actividad, duracion, clave = linea.split('|')
            seguridad = validar_contrasena(clave)
            salida.write(f"nombre: {usuario.capitalize()} - actividad: {actividad} - duracion: {duracion} - Contraseña: {seguridad}\n")
        except Exception as e:
            salida.write("Error en línea: " + linea)


