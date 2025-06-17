import pandas as pd

data = {"No.":["1", "2", "3", "4"],
        "Nombre":["María", "Pedro", "Juan", "Antonio"],
        "Edad":["15", "16", "15", "17"],
        "Carrera":["Ciencia de Datos", "Contabilidad", "Programación", "Recursos  Humanos"],
        "Promedio":["9.8", "7", "9", "8"]
        }

df = pd.DataFrame(data)
df['Promedio'] = pd.to_numeric(df['Promedio'])
calcular_pro = df['Promedio'].mean()
print("El promedio es", calcular_pro)
print("Tabla de datos:")
print(df.to_string(index=False))