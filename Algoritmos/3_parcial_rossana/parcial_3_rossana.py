import pandas as pd

from Algoritmos.cilo_for import calificaciones

colores=pd.Series(["rojo", "azul", "rosa", "morado"])

print(colores)
print()
materias=pd.Series({"ingles":10, "culrura":8, "lengua":6})

print(materias)
print(colores.size)

print(materias(["lengua", "cultura", "ingles"]))

calificaciones=pd.Series([6,7,8,10,8,10])

print(calificaciones)
print()
print(calificaciones*2)
