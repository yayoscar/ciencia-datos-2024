# 1. Verifica si alguien puede votar
if edad >= 18 and credencial == True:
    print("Puede votar")

# 2. Evalúa si un alumno califica para beca
if promedio > 8.5 or es_atleta == True:
    print("Califica para beca")

# 3. Corrección
if edad > 60 or (edad < 18 and vive_en_mexico):
    print("Cumple la condición")