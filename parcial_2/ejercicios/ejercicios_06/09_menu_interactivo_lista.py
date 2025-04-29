tareas = []
while True:
    print("\n--- Menu ---")
    print("1. agregar tarea")
    print("2. ver tareas")
    print("3. eliminar tareas (por nombre)")
    print("4. salir")
    opcion = input("elige una opcion: ")
    if opcion == "1":
          tarea = input("escribe la nueva tarea: ")
          tareas.append(tarea)
          print("tarea agregada.")
    elif opcion == "2":
        if tareas:
            print("\nlista de tareas: ")
            for i, tarea in enumerate(tareas, start=1):
                print(f"{i}. tarea")
            else:
                print("no hay tareas.")
    elif opcion == "3":
            nombre_tarea = input("escribe el nombre de la tarea a eliminar: ")
            if nombre_tarea in tareas:
                tareas.remove(nombre_tarea)
                print("tarea eliminada.")
            else:
                print("tarea no encontrada.")
    elif opcion == "4":
         print("¡hasta luego!")
         break
    else:
         print("opcion no valida. intentab de nuevo.")