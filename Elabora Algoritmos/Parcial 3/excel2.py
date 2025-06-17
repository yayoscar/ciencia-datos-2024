import pandas as pd

ruta = "detalle_calificaciones.xlsx"
df = pd.read_excel(ruta)

if not {"NO CONTROL", "CALIFICACION", "NOMBRE"}.issubset(df.columns):
    raise ValueError("Faltan columnas necesarias en el archivo Excel.")

df = df.set_index("NO CONTROL")


promedio = df["CALIFICACION"].mean()

df_10 = df[df["CALIFICACION"] == 10]

numeros_control = [22323050720022, 22323050720283]
df_busqueda = df[df.index.isin(numeros_control)]

num_filas = len(df)

repeticiones = df["NOMBRE"].value_counts()
num_nombres_unicos = len(repeticiones)

print("Promedio de calificaciones: {:.2f}".format(promedio))
print("\n--- Alumnos con calificación 10 ---\n", df_10)
print("\n--- Alumnos encontrados por número de control ---\n", df_busqueda)
print("\nTotal de registros:", num_filas)
print("\n--- Repeticiones de nombres ---\n", repeticiones)
print("\nNúmero total de nombres únicos:", num_nombres_unicos)
