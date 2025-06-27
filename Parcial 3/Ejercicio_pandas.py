import pandas as pd
animales = ("Conejo", "Cisne", "Chita", "Delfín", "Zorro del desierto", "Panda", "Huron")
indice = ["A01","A02","A03","A04","A05","A06","A07"]
serie = pd.Series(data=animales, index=indice)
print (serie)


