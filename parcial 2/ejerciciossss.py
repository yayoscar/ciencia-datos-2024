def calcular_promedio(notas_str):
    notas = [float(nota) for nota in notas_str.split(',')]
    return round(sum(notas) / len(notas), 2)

def validar_contrasena(contrasena):
    if (len(contrasena) >= 8 and
        any(c.isupper() for c in contrasena) and
        any(c.isdigit() for c in contrasena)):
        return "Fuerte"
    return "Débil"

with open("temperaturas.txt", "r") as archivo:
    lineas = temperaturas.readlines()

with open("reporte_temperaturas.txt", "w") as salida:
    for linea in lineas:
        try:
            nombre, calificaciones, clave = linea.strip().split('|')
            promedio = calcular_promedio(calificaciones)
            seguridad = validar_contrasena(clave)
            salida.write(f"Nombre: {nombre} - Promedio: {promedio} - Contraseña: {seguridad}\n")
        except Exception as e:
            salida.write("Error en línea: " + linea)