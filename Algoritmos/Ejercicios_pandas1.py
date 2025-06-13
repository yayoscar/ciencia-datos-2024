import pandas as pd
datos=['Unicornio', 'Panda', 'Rinoceronte', 'Pez', 'Gato', 'Tortuga']
indices=["A01", "A02", "A03", "A04", "A05", "A06"]
series=pd.Series(data=datos,index=indices)
print(series)