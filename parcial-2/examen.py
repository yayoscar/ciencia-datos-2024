
def validar_contraseña(contraseña):
    if (len(contraseña) >= 8 and
        any (c.isupper() for c in contraseña) and
        any (c.isdigit() for c in contraseña)):
        return "Fuerte"
    return "Debil"

def formatear_linea(lineas):
    with open("actividades.txt", "r") as archivo:
        lineas = archivo.readlines()

    with open("actividades_validado.txt","w") as salida:
        for linea in lineas:
           try:
              nombre, actividad, tiempo, contraseña = linea.strip().split('|')
              nombre_capitalizado = nombre.capitalize()
              seguro = validar_contraseña(contraseña)
              salida.write(f" {nombre_capitalizado} realizo {actividad} por {tiempo}mn-Contraseña: {seguro}\n")
           except Exception as e:
              salida.write("Error en linea: "+ linea)
with open("actividades.txt", "r") as archivo:
    lineas = archivo.readlines()
print(formatear_linea(lineas=lineas))