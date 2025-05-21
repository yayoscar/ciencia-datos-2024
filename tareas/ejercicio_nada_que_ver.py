
medidas= [177.8,175.0,166.9,186.5]
print(medidas)
medidas.sort()
for medida in medidas:
    print(medidas)

persona= "sarah"
print(persona.capitalize())



tem = 32
print("--------------------")
print("f   c")
print("--------------------")
while tem<73:
    print(tem,"   ", int((tem-32)*5/9))
    tem = tem+1
print("--------------------")

 leer_temperaturas(temperaturas .txt):
    temperaturas = []
    with open(temperaturas.txt, newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            try:
                temp = float(fila['temperatura'])
                temperaturas.append(temp)
            except ValueError:
                print(f"Valor no válido en la fila: {fila}")
    return temperaturas

def calcular_estadisticas(temperaturas):
    return {
        'mínimo': min(temperaturas),
        'máximo': max(temperaturas),
        'promedio': statistics.mean(temperaturas),
        'mediana': statistics.median(temperaturas),
        'desviación estándar': statistics.stdev(temperaturas)
    }

def generar_reporte(estadisticas, nombre_archivo_reporte):
    with open(nombre_archivo_reporte, 'w', encoding='utf-8') as reporte:
        reporte.write("REPORTE ESTADÍSTICO DE TEMPERATURAS\n")
        reporte.write("="*40 + "\n")
        for clave, valor in estadisticas.items():
            reporte.write(f"{clave.capitalize():<20}: {valor:.2f} °C\n")
    print(f"Reporte generado: {nombre_archivo_reporte}")


archivo_entrada = 'temperaturas.csv'
archivo_salida = 'reporte_temperaturas.txt'

temperaturas = leer_temperaturas(archivo_entrada)

if temperaturas:
    estadisticas = calcular_estadisticas(temperaturas)
    generar_reporte(estadisticas, archivo_salida)
else:
    print("No se encontraron temperaturas válidas.")

