tareas = []

while True:
    print( "¿que deseas hacer?")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Eliminar tarea")
    print("4. Salir")

    opcion = input("Elige una opción (1-4): ")

    if opcion == "1":
        tarea = input("Escribe la tarea que quieres agregar: ")
        tareas.append(tarea)
        print("Tarea agregada.")

    elif opcion == "2":
        if tareas:
            print("Lista de tareas:")
            for indice, tarea in enumerate(tareas, 1):
                print(f"{indice}. {tarea}")
        else:
            print("No hay tareas.")

    elif opcion == "3":
        eliminar = input("Escribe el nombre de la tarea a eliminar: ")
        if eliminar in tareas:
            tareas.remove(eliminar)
            print("Tarea eliminada.")
        else:
            print("La tarea no existe o la escribio mal.")

    elif opcion == "4":
        print("cerrando el programa(que tenga un buen dia)...")
        break

    else:
        print("Opción no válida. Intenta de nuevo.")
