import csv
import os

def clacular_progreso(meta,semanas,aporte,sem_trans):
    if sem_trans > semanas:
        return "Error: Las semanas transcurridas no pueden ser mayores al tiempo total."

    ahorro_esp = (meta/semanas) * sem_trans
    ahorro_real = aporte * sem_trans
    falta = meta - ahorro_real
    porcentaje = (ahorro_real / meta) * 100
    mensaje=""
    if ahorro_real >= ahorro_esp:
        mensaje = "Vas por buen camino"
    else:
        mensaje = "Debes acelerar tu ahorro"
    resultado =(
        f"Has ahorrado: ${ahorro_real:.2f}\n"
        f"Te falta: ${falta:.2f}\n"
        f"Progreso: {porcentaje:.2f}%\n"
        f"{mensaje}"
    )
    return resultado

def guardar_csv(aporte):
    fila = [aporte]
    with open("datos.csv","a", newline='') as archivo:
        escribir = csv.writer(archivo)
        escribir.writerow(fila)