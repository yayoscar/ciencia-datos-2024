def validar_contraseña(contrasenia):
    si_mayuscula=any(i.supper() for i in contrasenia)
    si_numero = any(i.isdigit() for i in contrasenia)
    cantidad_valida= len(contrasenia) > 8
    return si_mayuscula and si_numero and cantidad_valida

def formatear_linea(lineas):
        archivo = open("actividades.txt", "r")
        archivo.readlines()
with open("actividades.txt", "w") as salida:
    try:
        Nombre, Actividad, Duracion, Contraseña = lineas.strip().split("|")
        si_segura = validar_contraseña(contrasenia)
        salida.write(f"Nombre, {Nombre}, Actividad, {Actividad}, Duracion, {Duracion}, Contraseña, {si_segura}\n")

