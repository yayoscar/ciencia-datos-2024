mensaje = "Ingresa una tarea"
todos = []
while True:
     accion_usuario=input("indica que accion quieres realizar agregar/mostrar/listar/editar/salir ")
     accion_usuario = accion_usuario.strip()
     accion_usuario = accion_usuario.lower()
     match accion_usuario:
         case "agregar":
             todo = input(mensaje)
             todos.append(todo)
         case "editar":
             posicion = input("¿Que posicion deseas editar? ")
             print(todos[posicion])
         case "mostrar":
             for elemento in todos:
                 elemento = elemento.title()
                 print(todos)
         case "salir":
             break


print("adios")


