tareas = []
while True:
    print("\n ---menu de tareas---")
    print("1. agregar tarea")
    print("2. ver tareas")
    print("3. eliminar tarea")
    print("4. salir")
    opcion = input("elige una opcion (1-4):")
    if opcion == "1":
        tarea = input("escribe la tarea que quires agregar:")
        tareas.append(tarea)
        print("tarea agrgada.")
    elif opcion == "2":
        if tareas:
            print("f\nlista de tareas:")
            for i, tareas in enumerate(tareas, 1):
                print(f"{1}, {tareas}")
        else:
            print("no hay tareas.")
    elif opcion == "3":
        tarea_a_eliminar = input("escribe el nombre exacto de la tera a eliminar:")
        if tarea_a_eliminar in tareas:
            tareas.remove(tarea_a_eliminar)
            print("tarea eliminada")
        else:
            print("la tarea no se encontro.")
    elif opcion == "4":
        print("saliendo del programa...")
        break
    else:
        print("opcion no valida. intenta de nuevo")