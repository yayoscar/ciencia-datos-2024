def extraer_datos(nombre_archivo):
    datos = []
    with open("temperaturas.txt", 'r') as archivo:
        for linea in archivo:
            hora, temperatura, sensor = linea.strip().split(',')
            datos.append((hora.strip(), float(temperatura.strip()), sensor.strip()))
    return datos

def minimo_maximo(datos):
    temperaturas = [temp for _, temp, _ in datos]
    promedio = sum(temperaturas) / len(temperaturas)
    minima = min(temperaturas)
    maxima = max(temperaturas)
    return promedio, minima, maxima

def reporte(nombre_archivo_entrada, datos, promedio, minima, maxima):
    with open("reporte_temperaturas.txt", "w") as archivo:
        archivo.write(f"Archivo: {nombre_archivo_entrada}")
        archivo.write("Formato:\nHora, Temperatura,")
        for hora, temp, sensor in datos:
            archivo.write(f"{hora}, {temp}, {sensor}")
        archivo.write("\nResumen estadístico:\n")
        archivo.write(f"Promedio: {promedio:.1f}")
        archivo.write(f"Mínima: {minima:.1f}")
        archivo.write(f"Máxima: {maxima:.1f}")

nombre_archivo = "temperaturas.txt"
datos = extraer_datos(nombre_archivo)
promedio, minima, maxima = minimo_maximo(datos)
reporte(nombre_archivo, datos, promedio, minima, maxima)