import pandas as pd

# 1. Leer el archivo de Excel
archivo = "alumnos_cbtis.xlsx"  # Asegúrate de que el archivo exista en el mismo directorio
df = pd.read_excel(archivo)

# 2. Convertir el índice al número de control
df.set_index("No.Control", inplace=True)

# 3. Calcular el promedio general de todos los alumnos
promedio_general = df.mean(numeric_only=True).mean()
print(f"Promedio general de todos los alumnos: {promedio_general:.2f}")

# 4. Seleccionar alumnos con todas sus calificaciones en 10
df_10 = df[(df.select_dtypes(include="number") == 10).all(axis=1)]
print("\nAlumnos con todas las calificaciones en 10:")
print(df_10)

# 5. Guardar este DataFrame en un archivo nuevo
df_10.to_excel("alumnos_10.xlsx")
print("\n Archivo 'alumnos_10.xlsx' guardado.")

# 6. Buscar alumnos con número de control específico
controles = ["22323050720022", "22323050720283"]
busqueda = df.loc[df.index.astype(str).isin(controles)]
print("\nBúsqueda de alumnos con número de control específico:")
print(busqueda)

# 7. Guardar resultados de la búsqueda
busqueda.to_excel("busqueda_alumnos.xlsx")
print("Archivo 'busqueda_alumnos.xlsx' guardado.")

# 8. Cantidad de filas del archivo (alumnos)
total_filas = len(df)
print(f"\nCantidad total de filas (alumnos): {total_filas}")

# 9. Veces que se repite cada nombre
repeticiones_nombre = df['Nombre'].value_counts()
print("\nRepeticiones por nombre:")
print(repeticiones_nombre)

# 10. Cantidad de nombres únicos
nombres_unicos = df['Nombre'].nunique()
print(f"\nCantidad de nombres únicos: {nombres_unicos}")
