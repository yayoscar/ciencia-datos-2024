def promedio(lista):
    listas=[float(nota) for nota in lista.split(',')]
    return round(sum(listas) / len(listas), 2)

def extraer_nombre_archivo(nombre_archivo):
    if nombre_archivo:
        return "teperatura maxima"
    else:
        return "teperatura minima"

with open("temperatura.txt","r") as archivo:
    listas= archivo.readlines()

with open("reporte_temperaturas.txt", "w") as salida:
    for lista in listas:
        try:
            nombre, calificaciones, clave = lista.strip().split('|')
            promedio = promedio(calificaciones)
            nombres = extraer_nombre_archivo(temperatura)
            salida.write(f"Nombre: {nombre} - Promedio: {promedio} - temperatura: {nombres}\n")
        except Exception as e:
            salida.write("Error en línea: " + lista)