tareas = []

while True:
  print("\nMenú:")
  print("1. Agregar tarea")
  print("2. Ver tareas")
  print("3. Eliminar tarea (por nombre)")
  print("4. Salir")

  opcion = input("Selecciona una opción: ")

  if opcion == "1":
    tarea = input("Ingresa la tarea: ")
    tareas.append(tarea)
    print("Tarea agregada.")
  elif opcion == "2":
    if tareas:
      print("\nLista de tareas:")
      for i, tarea in enumerate(tareas):
        print(f"{i+1}. {tarea}")
    else:
      print("No hay tareas en la lista.")
  elif opcion == "3":
    if tareas:
      tarea_eliminar = input("Ingresa el nombre de la tarea a eliminar: ")
      if tarea_eliminar in tareas:
        tareas.remove(tarea_eliminar)
        print("Tarea eliminada.")
      else:
        print("La tarea no se encuentra en la lista.")
    else:
      print("No hay tareas en la lista.")
  elif opcion == "4":
    print("Saliendo del programa...")
    break
  else:
    print("Opción inválida.")