numero_alumnos = int(input("Número de alumnos: "))
calificacion_mayor = 0
calificacion_menor = 0
numero_aprobados = 0
numero_reprobados = 0
suma_calificaciones = 0
lista_nombres = []
lista_calificaciones = []

nombre_alumno = input("Nombre del alumno: ")
while True:
    calificacion = int(input("Calificación de alumno: "))
    if calificacion <0 or calificacion> 10:
        print(f"UPS, ERROR!, DIGITE DE NUEVO LA CALIFICACIÓN DE {nombre_alumno}")
    else:
        break
calificacion_mayor = calificacion
calificacion_menor = calificacion
suma_calificaciones += calificacion
lista_nombres.append(nombre_alumno)
lista_calificaciones.append(calificacion)
if calificacion > 6.00:
    numero_aprobados +=1
else:
    numero_reprobados +=1
if calificacion > calificacion_mayor:
    calificacion_mayor = calificacion
if calificacion < calificacion_menor:
    calificacion_menor = calificacion
for n in range(numero_alumnos-1):
    nombre_alumno = input("Nombre del alumno: ")
    while True:
        calificacion = int(input("Calificación de alumno: "))
        if calificacion < 0 or calificacion > 10:
            print(f"UPS, ERROR!, DIGITE DE NUEVO LA CALIFICACIÓN DE {nombre_alumno}")
        else:
            break
    suma_calificaciones += calificacion
    lista_nombres.append(nombre_alumno)
    lista_calificaciones.append(calificacion)
    if calificacion > 6.00:
        numero_aprobados += 1
    else:
        numero_reprobados += 1
    if calificacion > calificacion_mayor:
        calificacion_mayor = calificacion
    if calificacion < calificacion_menor:
        calificacion_menor = calificacion
promedio = suma_calificaciones/ numero_alumnos
print(f"Promedio grupal: {round(promedio, 2)}")
print(f"Alumnos aprobados: {numero_aprobados}")
print(f"Alumnos reprobados: {numero_reprobados}")
print(f"Mayor promedio:{calificacion_mayor}" )
print(f"Menor promedio:{calificacion_menor}" )
