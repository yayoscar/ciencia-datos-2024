lista = open("lista.txt", "r")
num = int(lista.readline())
contador = 0
total = 0
alumnos = []
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
        if calificacion > 100.00:
            error = f"ERROR!, POR FAVOR INGRESE NUEVAMENTE LA CALIFICACIÓN DE {alumno}"
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
promedio = total / num
if continuar:
    print(error)
print(f"Promedio grupal: {round(promedio, 2)}")
print(f"Alumnos aprobados: {len(aprobados)}")
print(f"Alumnos reprobados: {len(reprobados)}")
print("Mayor promedio:", max(calificaciones))
print("Menor promedio:", min(calificaciones))
# Al final no pudimos imprimir al alumno junto con la calificación