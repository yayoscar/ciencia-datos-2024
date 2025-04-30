numero_alumno = int(input("Número de alumnos: "))
calificacion_mayor=0
calificacion_menor=0
suma_calificacion=0
nuemros_aprobados=0
numeros_reprobados=0
lista_nombres= []
lista_calificacion= []

nombre_alumno=input("Nombre del alumno: ")
while True:
    calificacion=int(input("Calificacion del alumno"))
    if calificacion <0 or calificacion > 100:
        print("UPS, ERROR!, DIGITE DE NUEVO LA CALIFICACION")
    else:
        break
calificacion_mayor=calificacion
calificacion_menor=calificacion
suma_calificacion += calificacion
lista_nombres.append("Nombre del alumno")
lista_calificacion.append(calificacion)
if calificacion >=60:
    numeros_aprobados += 1
else:
    numero_reprobados += 1

for n in range(numero_alumno):