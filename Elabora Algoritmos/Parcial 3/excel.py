import pandas as pd

archivo = "Escuela.xlsx"

df_familia = pd.read_excel(archivo, sheet_name="Hoja1")
print("Familia:")
print(df_familia)
print()

df_animales = pd.read_excel(archivo, sheet_name="Hoja2")
print("Escuela:")
print(df_animales)