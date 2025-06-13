import pandas as pd
datos=[10,9,7,8,5,6,9,10,8]
datos.sort()
series=pd.Series(data=datos)
print(series)
print(series.std())
print(series.mean())

