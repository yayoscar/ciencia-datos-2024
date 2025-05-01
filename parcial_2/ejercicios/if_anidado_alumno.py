calificacion = int(input("Ingresa tu calificación: "))
if calificacion >= 6:
    calificacion = True
    if calificacion == True:
     asistencia = int(input("¿Cuantas veces asististe entre 0-100? "))
     if asistencia == 100:
            print("Excelente estudiante")
     else:
         print("Buen estudiante")
else:
    print("Reprobaste")