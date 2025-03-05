tareas = []

while True:
    print("\n--- MENÚ DE TAREAS ---")
    print("1. añadir tarea")
    print("2. Ver tus tareas")
    print("3. Eliminar una tarea")
    print("4. Salir")

    opcion = input("elige una opción (1-4): ")

    if opcion == "1":
        nueva_tarea = input("escribe la nueva tarea: ")
        tareas.append(nueva_tarea)
        print("¡Listo! tarea agregada.")

    elif opcion == "2":
        print("\n TUS TAREAS:")
        if tareas:
            for t, tarea in enumerate(tareas):
                print(f"{t+1}. {tarea}")
        else:
            print("aun no hay tareas")

    elif opcion == "3":
        eliminar = input("escribe el nombre especifico de la tarea que deseas borrar: ")
        if eliminar in tareas:
            tareas.remove(eliminar)
            print(" Tarea eliminada")
        else:
            print(" No se encontró esa tarea.")

    elif opcion == "4":
        print("¡Hasta luego!!!!")
        break

    else:
        print(" Opción no válida. Intenta de nuevo.")