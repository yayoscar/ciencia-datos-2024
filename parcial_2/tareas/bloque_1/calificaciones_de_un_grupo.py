lista = open('lista.txt', 'r')
num = int(lista.readline())
contador = 0
total = 0
alumnos = []
errores = ''
aprobados = []
reprobados = []
calificaciones = []
ambos = []
continuar = False
error = ''
while contador< num:
    alumno = lista.readline()
    alumnos.append(alumno)
    calificacion = float(lista.readline())
    if calificacion>= 60.00:
        aprobados.append(alumno)
        calificaciones.append(calificacion)
        if calificacion > 100.00 or calificacion < 0:
            error = f"UPS, ERROR!, DIGITE DE NUEVO LA CALIFICACIÓN DE {alumno}"
            aprobados.remove(alumno)
            errores += error
            continuar = True
            calificaciones.remove(calificacion)
            aprobados.append(alumno)
    else:
        reprobados.append(alumno)
        calificaciones.append(calificacion)
    ambos.append(f"{alumno}, {calificacion}")
    if calificacion > 100.00:
        nose = "Esto es solo para que no haga nada"
    else:
        total += calificacion
        num -= 1
    contador +=1
for alumno, calificacion in zip(alumnos, calificaciones):
    ambo = str(calificacion) + alumno
    ambos.append(ambo)
promedio = total / num
if continuar:
    print(errores)
print(f"Promedio grupal: {round(promedio, 2)}")
print(f"Alumnos aprobados: {len(aprobados)}")
print(f"Alumnos reprobados: {len(reprobados)}")
print("Mayor promedio:", max(calificaciones))
print("Menor promedio:", min(calificaciones))
#No supe como hacer que pusiera al alumno con mayor y menor promedio :(
