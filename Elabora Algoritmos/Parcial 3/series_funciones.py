import pandas as pd

cali = pd.Series([10,9,8,7,6,4,9])

print(cali.sum())
print(cali.max())
print(cali.min())
print()

materias = pd.Series (["P. Matemático", "LyC", "CS", "Elabora", "Codifica", "Inglés", "Cultura dig"])
print(materias)
print()

print(cali*2)