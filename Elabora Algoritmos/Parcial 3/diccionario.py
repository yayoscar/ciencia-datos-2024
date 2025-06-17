import pandas as pd

colores = pd.Series (["rojo", "azul", "verde", "amarillo"])

print(colores)
print()
materias = pd.Series({"Pensamiento mat":9, "Cultura dig":10, "Inglés":7})
print(materias)

print(colores.size)

print(materias[["Pensamiento mat", "Cultura dig"]])