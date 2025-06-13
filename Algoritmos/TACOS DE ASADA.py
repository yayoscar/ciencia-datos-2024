import pandas as pd


path= "detalle_calificacionesok.xlsx"


dataframe= pd.read_excel(path,index_col= "NO CONTROL")
print(dataframe)
print()

suma=dataframe['CALIFICACION'].sum()
prom=dataframe['CALIFICACION'].mean()
print(prom)

may=dataframe["CALIFICACION"]==10


df_may = dataframe[may]
print(df_may)
print()
print(dataframe.loc[22323050720022])
print()
print(dataframe.loc[22323050720283])
print()

print(dataframe.NOMBRE.count())
print()
print(dataframe.NOMBRE.value_counts())

