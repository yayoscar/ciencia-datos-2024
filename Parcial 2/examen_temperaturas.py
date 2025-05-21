def c_promedio(lista):
    lista_p = float(sum(lista)/len(lista))
    return lista_p


def extraer_nombre_archivo(nombre_archivo):
    nombres_c = [str(nombre_archivo)for nombre in nombre_archivo.capitalize(',') and nombre_archivo.slice[-1:-4]]


with open("temperaturas.txt", "r") as archivo:
    lineas = archivo.readlines()

with open("reporte_temperaturas.txt", "w") as salida:
    for linea in lineas:
        try:
            promedio = c_promedio()
            t_mx = max(c_promedio())
            t_mn =

