import datetime

# Lista para almacenar tareas
tareas = []

# Función para agregar tarea
def agregar_tarea():
    nombre = input("Ingrese el nombre de la tarea: ")
    fecha_str = input("Ingrese la fecha y hora (formato: AAAA-MM-DD HH:MM): ")
    try:
        fecha = datetime.datetime.strptime(fecha_str, "%Y-%m-%d %H:%M")
        tareas.append({"nombre": nombre, "fecha": fecha})
        print("Tarea agregada con éxito.\n")
    except ValueError:
        print("Formato de fecha incorrecto. Intente nuevamente.\n")

# Función para mostrar tareas
def mostrar_tareas():
    if not tareas:
        print("No hay tareas pendientes.\n")
        return
    print("Tareas pendientes:")
    for i, tarea in enumerate(tareas, 1):
        print(f"{i}. {tarea['nombre']} - {tarea['fecha'].strftime('%Y-%m-%d %H:%M')}")
    print()

# Función para verificar tareas próximas
def verificar_alertas():
    ahora = datetime.datetime.now()
    for tarea in tareas:
        tiempo_restante = tarea["fecha"] - ahora
        if datetime.timedelta(0) <= tiempo_restante <= datetime.timedelta(hours=1):
            print(f"¡Alerta! La tarea '{tarea['nombre']}' está programada para las {tarea['fecha'].strftime('%H:%M')} (en menos de 1 hora)")
    print()

# Menú principal
while True:
    print("=== MENÚ DE TAREAS ===")
    print("1. Agregar nueva tarea")
    print("2. Mostrar tareas pendientes")
    print("3. Verificar alertas de tareas próximas")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_tarea()
    elif opcion == "2":
        mostrar_tareas()
    elif opcion == "3":
        verificar_alertas()
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Intente de nuevo.\n")