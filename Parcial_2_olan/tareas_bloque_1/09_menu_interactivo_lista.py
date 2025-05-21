tareas = []

while True:
    print("\n--- MENÚ DE TUS TAREAS DE LA ESCUELA 🥺🥺🥺---")
    print("1. Agregar tarea")
    print("2. Ver tus tareas")
    print("3. Eliminar tarea")
    print("4. Salir")

    opcion = input("Elige una opción (1-4): ")

    if opcion == "1":
        nueva_tarea = input("Escribe la nueva tarea: ")
        tareas.append(nueva_tarea)
        print("✅ Tarea agregada.")

    elif opcion == "2":
        print("\n📋 TUS TAREAS:")
        if tareas:
            for i, tarea in enumerate(tareas):
                print(f"{i+1}. {tarea}")
        else:
            print("No hay tareas aún.")

    elif opcion == "3":
        eliminar = input("Escribe el nombre exacto de la tarea a eliminar: ")
        if eliminar in tareas:
            tareas.remove(eliminar)
            print("🗑️ Tarea eliminada.")
        else:
            print("❌ No se encontró esa tarea.")

    elif opcion == "4":
        print("¡Hasta luego!")
        break

    else:
        print("⚠️ Opción no válida. Intenta de nuevo.")