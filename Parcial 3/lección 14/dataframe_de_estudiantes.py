#Data frame de estudiantes

import pandas as pd
path = "detalle_calificacionesokexel.xlsx"
datos = pd.read_excel(path,index_col="NO CONTROL")
print(datos)
print()
print("     Promedios    ")
prom=datos["CALIFICACION"].mean()
print("Promedio general:",prom)
print("Las calificaciones mayores de diez:")
may = datos["CALIFICACION"]==10
df_may=datos[may]
print(df_may)
print()
print("Localizar los datos de 22323050720022")
print(datos.loc[22323050720022])
print()
print("Localizar los datos de 22323050720283")
print(datos.loc[22323050720283])
print()
filas = len(datos)
print("La cantidad de filas es:",filas)
nombres_rep =datos["NOMBRE"].value_counts()
print("Los numeros repetidos son:")
print(nombres_rep)
nombres = len(datos["NOMBRE"].unique())
print("La cantidad de nombres unicos es:",nombres)
