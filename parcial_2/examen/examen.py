def calcular_temperatura_ciudad(notas_str):
    notas = [float(nota) for nota in notas_str.split(',')]
    return round(sum(notas) / len(notas), 2)

def validar_contrasena(contrasena):
    # Verifica si la contraseña es fuerte
    if (len(contrasena) >= 8 and
        any(c.isupper() for c in contrasena) and
        any(c.isdigit() for c in contrasena)):
        return "Fuerte"
    return "Débil"

# Abre el archivo de temperaturas para leer
with open("temperaturas.txt.py", "r") as archivo:
    lineas = archivo.readlines()

# Abre el archivo para escribir el reporte
with open("reporte_temperaturas.txt", "w") as salida:
    for linea in lineas:
        try:
            # Separa los datos por el carácter '|' y elimina espacios
            nombre, temperaturas, clave = linea.strip().split('|')

            # Calcula el promedio (debes tener una función llamada temperatura_ciudad)
            promedio = calcular_temperatura_ciudad(temperaturas)

            # Valida la seguridad de la contraseña
            seguridad = validar_contrasena(clave)

            # Escribe el resultado en el archivo
            salida.write(f"Nombre: {nombre} - Promedio: {promedio} - Contraseña: {seguridad}\n")

        except Exception as e:
            # Si algo falla, escribe un mensaje de error
            salida.write("Error en línea: " + linea + "\n")