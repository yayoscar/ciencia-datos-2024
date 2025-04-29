numero_alumno=int(input("Numero de Alumnos: "))
calificacion_mayor=0
calicacion_menor=0
suma_calificacion=0
numero_aprobados=0
numero_reprobados=0
lista_nombres=[]
lista_calificacion=[]
lista_mayores=[]
lista_menores=[]

nombre_alumno=input("Nombre del alumno:")
while True:
    calificacion=int(input("Calificacion del alumno: "))
    if calificacion <0 or calificacion > 100:
        print("UPS, ERROR!, DIGITE DE NUEVO LA CALIFICACION")
    else:
        break
calificacion_mayor=calificacion
calicacion_menor=calificacion
suma_calificacion += calificacion
lista_nombres.append(nombre_alumno)
lista_calificacion.append(calificacion)
if calificacion>=60:
    numero_aprobados += 1
else:
    numero_reprobados +=1

for n in range(numero_alumno-1):
    nombre_alumno = input("Nombre del alumno:")
    while True:
        calificacion = int(input("Calificacion del alumno: "))
        if calificacion < 0 or calificacion > 100:
            print("UPS, ERROR!, DIGITE DE NUEVO LA CALIFICACION")
        else:
            break
    if calificacion>calificacion_mayor:
        calificacion_mayor=calificacion
    if calificacion<calicacion_menor:
        calicacion_menor=calificacion
    suma_calificacion += calificacion
    lista_nombres.append(nombre_alumno)
    lista_calificacion.append(calificacion)
    if calificacion >= 60:
        numero_aprobados += 1
    else:
        numero_reprobados += 1

promedio=suma_calificacion/numero_alumno

for index,valor in enumerate(lista_calificacion):
    if valor==calificacion_mayor:
        lista_mayores.append(lista_nombres[index])
    if valor==calicacion_menor:
        lista_menores.append(lista_nombres[index])

lista_mayores.sort()
lista_menores.sort()

print(f"Promedio total del grupo: {promedio}")
print(f"Cantidad de alumnos aprobados: {numero_aprobados}")
print(f"Cantidad de alumnos reprobados: {numero_reprobados}")
print(f"Alumno con la calificación mayor: {lista_mayores[0]}")
print(f"Alumno con la calificación menor: {lista_menores[0]}")

