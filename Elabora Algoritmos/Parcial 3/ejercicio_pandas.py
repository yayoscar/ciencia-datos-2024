import pandas as pd

animales=["Panda", "Koala", "Tigre", "Oso", "Conejo", "Gato", "Perro"]
indices = ["A01", "A02", "A03", "A04", "A05", "A06", "A07"]

serie=pd.Series(data=animales, index=indices)
print("La tabla es:")
print(serie)