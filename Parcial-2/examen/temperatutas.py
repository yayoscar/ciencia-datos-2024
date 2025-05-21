def calcula_temperatura(promedios_str):
    promedios = [float(promedio) for promedio in promedios_str.split(',')]
    return round(sum(promedios) / len(promedios),2)
with open("temperaturas.txt", "r") as archivo:
    lineas = archivo.readlines()



with open("reporte_temperaturas.txt", "w") as salida:
    for linea in lineas:
        try:
            hora, calificaciones, archivo = linea.strip().split('|')
            temperatura = calcula_temperatura(calificaciones)
            seguridad = validar_texto(archivo)
            salida.write(f"Hora: {hora} - Promedio: {calificaciones} - Reporte: {seguridad}\n")
        except Exception as e:
            salida.write("Error en línea: " + linea)
