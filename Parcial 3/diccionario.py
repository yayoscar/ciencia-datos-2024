import pandas as pd

colores=pd.Series(["rosa,turquesa,azul,blanco"])

print(colores)
print()
materias=pd.Series({"Pensamiento mat":9,"Cultura dig" :10,"español":6})

print(materias)

print(colores.size)

print(materias[["Pensamiento mat", "Cultura dig"]]) #acceder a un valor almacenado
