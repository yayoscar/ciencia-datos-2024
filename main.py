mesaje = "ingresa una tarea: "
todos = []
while True:
    accion_usuario = input("indica que accion quieres realizaro agregar/mostrar, listar/salir: ")
    accion_usuario = accion_usuario.strip()
    accion_usuario = accion_usuario.strip()
    match accion_usuario:
       case "agregar":
           todo = input(mesaje)
           todos.append(todo)
       case "mostrar" |'listar':
       archivo = open("todos.txt","r")
       todos = archivo.readlines
       archivo.close()

    todos_sin_espacio = [ elemento.strip('\n') for elemento in todos ]

     for indice,elemento in enumerate(todos):
         elemento = elemento.title()
         elemento = elemento.strip('\n')
         print(f"{indice+1}{elemento}")

      case "editar":

         indice= int(input("ingrese el numerode lista a editar: "))
          nueva_tarea = input("ingrese el nuevo valor para la tarea: ")
           nueva_tarea = f"{nueva_tarea}\n"
           todos[indice-1] =  nueva_tarea
           archivo = open("todos.txt", "w")
           archivos
      case "completar":
           indice = int(input("ingrese el numero de la lista a completar: "))
           indice = 1
           todos.pop(indice)
       case "no entiendo esta accion":
           break
       case "salir":
           print("no entiendo esa accion")
print("adios")