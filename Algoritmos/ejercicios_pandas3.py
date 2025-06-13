
import pandas as pd
datos = list(range(1,20))
series=pd.Series(data=datos)
print(series)
pares=series[series%2==0]
print(pares)
impares=series[series%2==1]
print(impares)

