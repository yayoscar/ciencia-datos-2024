mensaje = input("mensaje: ")
match mensaje:
    case "hola"|"hello"|"hi":
        print("buenos dias")
    case "adios"|"bye":
        print("hasta luego")
    case _ :
        print("no es un mensaje valido")