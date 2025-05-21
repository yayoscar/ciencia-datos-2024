numero_alumno = int(input("Número de alumnos: "))
calificacion_mayor = 0
calificacion_menor = 0
suma_calificacion = 0
numero_aprobados = 0
numero_reprobados = 0

nombre_alumno = input("Nombre del alumno: ")
while True:
    calificacion = int(input("Calificacion del alumno: "))
    if calificacion <0 or calificacion > 100:
        print("UPS, ERROR!, POR FAVOR DIGITE DE NUEVO LA CALIFICACION")
    else:
        break
calificacion_mayor = calificacion
calificacion_menor = calificacion
suma_calificacion += calificacion
lista_nombres.append(nombre_alumno)