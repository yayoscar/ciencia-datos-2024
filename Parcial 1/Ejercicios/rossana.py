dia = int(input("Ingresa el día del mes (1-30): "))

if dia >= 1 and dia <= 7:
    fase = "Luna nueva"
    tarea = "Sembrar cultivos de raíz"
elif dia >= 8 and dia <= 14:
    fase = "Cuarto creciente"
    tarea = "Sembrar cultivos de hoja"
elif dia >= 15 and dia <= 21:
    fase = "Luna llena"
    tarea = "Cosechar y podar"
elif dia >= 22 and dia <= 30:
    fase = "Cuarto menguante"
    tarea = "Eliminar plagas y limpiar"
else:
    fase = "Día inválido"
    tarea = "No hay tarea agrícola"

print("Fase lunar:", fase)
print("Tarea agrícola recomendada:", tarea)