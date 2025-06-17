import pandas as pd

dato = "detalle_calificacionesok2.xlsx"
dataframe= pd.read_excel(dato,index_col="NO CONTROL")
print(dataframe)
print()
""""
suma=dataframe["promedio"].sum()
prom=dataframe["promedio"].mean()
print(suma)
print(prom)

may=dataframe["Edad"]>15

df_may=dataframe[may]
print(df_may)
print()
print(dataframe.loc[3])
print()
print(pd.read_excel(dato,index_col="Hoja2"))
print()
print(dataframe.Nombre.count())
print()

print(dataframe.Nombre.value_conuts())
"""""