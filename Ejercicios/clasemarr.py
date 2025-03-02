mensaje = "baax onda"
match mensaje:
    case "hola":
        print("Buenos dias")
    case "adios":
        print("Hasta luego")
    case _:
        print("No es un mensaje válido")
