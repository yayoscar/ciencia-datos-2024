seg_tierra = int(input("¿Cuántos segundos en la tierra son por 1 segundo en la nave? "))
seg_nave = int(input("¿Cuántos segundos se percibieron en la nave? "))
seg_ = seg_nave * seg_tierra
seg_totales = seg_
dias = 0
horas = 0
minutos = 0
while seg_totales >= 60:
    if seg_totales >= 60:
        seg_totales -= 60
        minutos += 1
        if minutos >= 60:
            horas += 1
            minutos -= 60
            if horas >=24:
                dias += 1
                horas -=24
print(f"""(Segundos totales: {seg_})
Días: {dias}
Horas: {horas}
Minutos: {minutos}
Segundos: {seg_totales}""")