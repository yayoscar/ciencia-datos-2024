import csv


def temperaturas(temperaturas):
    temperaturas =[]
    with open("temperaturas.txt")
        lector = csv.DictReader(temperaturas)
        for fila in lector
            try:
                tem = float(fila['temperaturas'])
                temperaturas.append(tem)
            except ValueError:
                print(f"valor no valido en filia:{fila}")
    return temperaturas
def calcular_estadisca(estadisca, reporte_temperaturas):