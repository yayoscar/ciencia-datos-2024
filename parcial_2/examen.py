def promedio(lista):
    return sum(lista) / len(lista) if lista else 0

def extraer_nombre_archivo(nombre_archivo):
    return nombre_archivo.split('.')[0].capitalize()

temperaturas = []
sensores = []

with open("temperaturas.txt", "r", encoding="utf8") as archivo:
    for linea in archivo:
        linea = linea.strip()
        if not linea:
            continue
        partes = linea.split("|")
        if len(partes) != 3:
            continue
        hora, temp_str, sensor_archivo = partes
        try:
            temp = float(temp_str)
            temperaturas.append(temp)
        except ValueError:
            continue
        sensores.append(extraer_nombre_archivo(sensor_archivo))

if temperaturas:
    promedio_temp = round(promedio(temperaturas), 1)
    max_temp = max(temperaturas)
    min_temp = min(temperaturas)
else:
    promedio_temp = max_temp = min_temp = 0

reporte = (
    f"Promedio: {promedio_temp}\n"
    f"Máxima: {max_temp}\n"
    f"Mínima: {min_temp}\n"
    f"Archivos: {', '.join(sensores)}\n"
)

with open("reporte_temperaturas.txt", "w", encoding="utf8") as salida:
    salida.write(reporte)

print("Reporte generado exitosamente en 'reporte_temperaturas.txt'")
