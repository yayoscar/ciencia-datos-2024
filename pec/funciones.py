import csv

RUTA = "datos.csv"


def leer_tareas(ruta_archivo=RUTA):
  try:
    with open(ruta_archivo, "r", newline='') as archivo_local:
      lector = csv.reader(archivo_local)
      return list(lector)
  except FileNotFoundError:
    return []

def guardar_tareas(todos_arg, ruta_archivo=RUTA):
  with open(ruta_archivo, "w", newline='') as archivo_local:
    escritor = csv.writer(archivo_local)
    escritor.writerows(todos_arg)

def calcular(precio,veces,meses):
  return int(precio)*int(veces)*int(meses)*4