import pandas as pd
from pandas import DataFrame

datos = {"Valor": [10, 9, 7, 8, 5, 6, 9, 10, 8]}
df = DataFrame(datos)
df_ordenado = df.sort_values(by="Valor")
des_est = df["Valor"].std()
promedio = df["Valor"].mean()
print("La desviación estándar es:", des_est)
print("El promedio es:", promedio)
print(df_ordenado)
# std() desviacion estandar