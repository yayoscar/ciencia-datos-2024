numero_alumno=int(input('numero de alumnos'))
calificacion_mayor=0
calificacion_menor=0
suma_calificacion=0
numero_aprobados=0
numero_reprobados=0
lista_calificacion=[]
lista_nombre=[]

nombre_alumno=input('nombre del alumno')
while True:
    calificacion=int(input('calificacion del alumno'))
    if calificacion <0 or calificacion > 100:
        print('ups,error,dijite de nuevo la calificacion')
    else:
        break
    calificacion_mayor=calificacion
    calificacion_menor=calificacion
    suma_calificacion=calificacion
    lista_calificacion.append(calificacion)
    lista_nombre.append(calificacion)
