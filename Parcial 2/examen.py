def promedio(lista):
    return sum(lista) / len(lista)

def extraer_nombre_archivo(nombre_archivo):
    return nombre_archivo.split('.')[0].capitalize()

def procesar_temperaturas():
    temperaturas = []
    nombres_archivos = []

    with open("temperaturas.txt", "r") as archivo:
        for linea in archivo:
            partes = linea.strip().split('|')
            if len(partes) == 2:
                hora_temp, archivo_sensor = partes
                hora, temp = hora_temp.split()
                temp = float(temp)
                temperaturas.append(temp)
                nombre_limpio = extraer_nombre_archivo(archivo_sensor)
                if nombre_limpio not in nombres_archivos:
                    nombres_archivos.append(nombre_limpio)

    with open("reporte_temperaturas.txt", "w") as salida:
        salida.write(f"Promedio: {promedio(temperaturas):.1f}\n")
        salida.write(f"Máxima: {max(temperaturas):.1f}\n")
        salida.write(f"Mínima: {min(temperaturas):.1f}\n")
        salida.write("Archivos: " + ", ".join(nombres_archivos) + "\n")
        procesar_temperaturas()
