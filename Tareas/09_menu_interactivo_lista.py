tareas = []
while True:
    print("\n--- Menú de Tareas ---")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Eliminar tarea")
    print("4. Salir")

    opcion = input("Selecciona una opción (1-4): ")

    if opcion == '1':
        tarea = input("Escribe la tarea a agregar: ")
        tareas.append(tarea)
        print("Tarea agregada.")
    elif opcion == '2':
        if tareas:
            print("\nLista de tareas:")
            for idx, tarea in enumerate(tareas, 1):
                print(f"{idx}. {tarea}")
        else:
            print("No hay tareas todavía.")
    elif opcion == '3':
        tarea_a_eliminar = input("Escribe el nombre exacto de la tarea a eliminar: ")
        if tarea_a_eliminar in tareas:
            tareas.remove(tarea_a_eliminar)
            print("Tarea eliminada.")
        else:
            print("La tarea no fue encontrada.")
    elif opcion == '4':
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Intenta de nuevo.")
