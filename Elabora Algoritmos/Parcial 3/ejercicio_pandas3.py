import pandas as pd

elementos = list(range(21))

serie = pd.Series(data=elementos)
print("La tabla:")
print(serie)
pares = serie[serie%2==0]
print("La tabla con números pares:")
print(pares)
impares = serie[serie%2==1]
print("La tabla con números impares:")
print(impares )