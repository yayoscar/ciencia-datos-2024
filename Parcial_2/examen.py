def validar_contraseña(clave):
    if (len(clave) >= 8 and
        any(c.isupper()for c in clave) and
        any(c.isdigit()for c in clave)):
        return "Contraseña Fuerte"
    return "Contraseña débil"


def formatear_linea(notas_str):
    notas = [float(nota) for nota in notas_str.split(',')]
    return notas

with open("actividades.txt","r") as archivo:
    lineas = archivo.readlines()

salida_texto=""
with open("actividades.txt", "w") as salida:
    for linea in lineas:
        try:
            nombre, clave,notas = linea.strip().split('|')
            seguridad = validar_contraseña(clave)
            salida_texto = (f"Nombre: {nombre.capitalize()} realizo: {notas} - Contraseña: {seguridad}\n")
        except Exception as e:
            salida.write("Error en línea: " + linea)

print(salida_texto)