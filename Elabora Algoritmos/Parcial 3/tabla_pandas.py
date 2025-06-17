A112 = ["Yazuri", "Gongora", 1234567890, "2do semestre", "Ciencia de Datos"]
A113 = ["Daniela", "Chin", 9876543210, "2do semestre", "Ciencia de Datos"]
A114 = ["Camila", "Martínez", 8236481740, "2do semestre", "Ciencia de Datos"]

# Agregar un dato más
A112.append(15)
A113.append(16)
A114.append(16)

print(A112)

alumnos = [A112, A113, A114]

print(alumnos)

import pandas as pd
df_alum = pd.DataFrame(alumnos, columns = ["Nombre", "Appellido", "No. Control", "Semestre", "Carrera", "Edad"])
print(df_alum)
print()

print(df_alum.sort_values("Edad", ascending = False))