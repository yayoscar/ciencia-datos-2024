def promedio(lista):
    sensores = [float(lis) for lis in lista.split(',')]
    return round(sum(sensores) / len(sensores), 2)

with open("temperaturas.txt", "r") as archivo:
    lineas = archivo.readlines()

with open("reporte_temperaturas.txt", "w") as salida:
    for linea in lineas:
        try:
            prom = linea.strip().split('|')
            promedios = promedio(prom)
            salida.write(f"Promedio:{promedios}\n")
        except Exception as e:
            salida.write("Error en línea: " + linea)