segtierra = int(input("¿Cúantos segundos en la tierra equivalen a un segundo en la nave?: "))
segnave = int(input("¿Cuántos segundos pasaron en la nave?: "))
segundos_totales = segtierra * segnave
minutos = 0
horas = 0
dias = 0
while segundos_totales >= 60:
   if segundos_totales >= 60:
       minutos += 1
       segundos_totales -= 60
       if minutos >= 60:
           horas += 1
           minutos -= 60
           if horas >= 24:
               dias += 1
               horas -= 24
print(f"""Días: {dias}
Horas: {horas}
Minutos: {minutos}
Segundos: {segundos_totales} 
""")