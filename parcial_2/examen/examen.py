def calcular_temperatura_ciudad(notas_str):
    notas = [float(nota) for nota in notas_str.split(',')]
    return round(sum(notas) / len(notas), 2)

def validar_contrasena(contrasena):
    if (len(contrasena) >= 8 and
        any(c.isupper() for c in contrasena) and
        any(c.isdigit() for c in contrasena)):
        return "Fuerte"
    return "Débil"

def obtener_temperaturas():
    with open("archivos/reporte_temperaturas.txt","r")as archivo:
        data = archivo.readlines()
    return data

temperaturas = obtener_temperaturas()
print(temperaturas)

with open("temperaturas.txt.py", "r") as archivo:
    lineas = archivo.readlines()

with open("reporte_temperaturas.txt.py", "w") as salida:
    for linea in lineas:
        try:
            nombre, temperaturas, clave = linea.strip().split('|')
            promedio = calcular_temperatura_ciudad(temperaturas)
            seguridad = validar_contrasena(clave)
            salida.write(f"Nombre: {nombre} - Promedio: {promedio} - Contraseña: {seguridad}\n")
        except Exception as e:
            salida.write("Error en línea: " + linea)