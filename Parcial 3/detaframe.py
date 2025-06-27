#Datos alumnos
A175=["Eusebio ", "Pool ", 24323050720213, "2do semestre","Ciencia de Datos"]
A174=["Yazuri ", " Gongora",24323050720191,"2do semestre", "Ciencia de Datos"]
A172=["Camila", "Martínez",517860318050609, "2do semestre", "Ciencia de Datos"]

A175.append(15)
A174.append(15)
A172.append(16)

alum=[A175,A174,A172]
print(alum)
import pandas as pd
df_alum=pd.DataFrame(alum,columns= ["Nombre", "Apellido","No.control","semestre","carrera","edad"])
print(df_alum)
print(df_alum.sort_values("edad", ascending=False))
