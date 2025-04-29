tareas = []

while True:
    print("\nMenú:")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Eliminar tarea")
    print("4. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        tarea = input("Introduce la tarea: ")
        tareas.append(tarea)
        print("Tarea agregada.")
    elif opcion == "2":
        if not tareas:
            print("No hay tareas.")
        else:
            print("\nTareas:")
            for i, tarea in enumerate(tareas):
                print(f"{i+1}. {tarea}")
    elif opcion == "3":
        if not tareas:
            print("No hay tareas para eliminar.")
        else:
            print("\nTareas:")
            for i, tarea in enumerate(tareas):
                print(f"{i+1}. {tarea}")
            try:
                eliminar = int(input("Introduce el número de la tarea a eliminar: ")) -1
                if 0 <= eliminar < len(tareas):
                    tarea_eliminada = tareas.pop(eliminar)
                    print(f"Tarea '{tarea_eliminada}' eliminada.")
                else:
                    print("Número de tarea inválido.")
            except ValueError:
                print("Entrada inválida. Introduce un número.")
    elif opcion == "4":
        print("Saliendo...")
        break
    else:
        print("Opción inválida.")