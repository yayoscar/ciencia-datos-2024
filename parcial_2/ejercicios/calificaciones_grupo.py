numero_alumno=int(input("Numero de Alumnos: "))
calificacion_mayor=0
calificacion_menor=0
suma_calificacion=0
numero_aprobados=0
numero_reprobados=0
lista_nombres=[]
lista_calificacion=[]
lista_mayores=[]
lista_menores=[]

nombre_alumno=input("Nombre del alumno: ")
while True:
    calificacion=int(input("Calificacion"))
    if calificacion <0 or calificacion > 100:
        print("UPS, ERROR, DIGITE DE NUEVO LA CALIFICACIÓN.")

    else:
        break
calificacion_mayor=calificacion
calificacion_menor=calificacion
suma_calificacion += calificacion
lista_nombres.append(nombre_alumno)
lista_calificacion.append(calificacion)
if calificacion>60:
    numero_reprobados=

for n in range(numero_alumno-1):
    nombre_alumno = input("Nombre del alumno: ")
    while True:
        calificacion = int(input("Calificacion del alumno: "))
        if calificacion <0 or calificacion > 100:
            print("UPS, ERROR, DIGITE DE NUEVO LA CALIFICACIÓN.")
        else:
            break
    if calificacion>calificacion_mayor:
        calificacion_mayor=calificacion
    if calificacion<calificacion_menor:
        calificacion_menor=calificacion
    suma_calificacion += calificacion
    lista_nombres.append(nombre_alumno)
    lista_calificacion.append(calificacion)
    if calificacion >=60:
        numero_aprobados += 1
    else:
        numero_reprobados += 1

promedio=suma_calificacion/numero_alumno

for index, valor in enumerate(lista_calificacion):
    if valor==calificacion_mayor:
        lista_mayores.append(lista_nombres[index])