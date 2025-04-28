tareas = []

while True:
    print("\n---Menú de tareas---")
    print("1-agregar tarea")
    print("2-Ver tareas")
    print("3-Eliminar tarea (por nombre)")
    print("4-salir")

    opcion = input("Elige una opción (1-4): ")

    if opcion == "1":
        tarea =input("ingresa el nombre de la tarea: ")
        tareas.append(tarea)
        print("tarea agregada :)")
    elif opcion == "2":
        if tareas:
            print("\nlista de tareas:")
            for i, tarea in enumerate(tareas, 1):
                print(f"{i}. {tarea}")

        else:
            print("no hay tareas")
    elif opcion == "3":
        nombre=input("ingresa el nombre de la tarea que quieres eliminar: ")
        if nombre in tareas:
            tareas.remove(nombre)
            print("tarea eliminada")
        else:
            print("tarea no encontrada")
    elif opcion == "4":
        print("saliendo del progrma...")
        break
    else:
        print("error, intentalo de nuevo.")



