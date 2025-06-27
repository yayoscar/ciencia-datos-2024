import pandas as pd

path = "Algoritmos.xlsx"
datos = pd.read_excel(path)
print(datos)
print()
print(pd.read_excel(path,sheet_name="Hoja2"))