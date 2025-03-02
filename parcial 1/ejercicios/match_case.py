mensaje =input("baax onda")
match  mensaje :
    case "hola"|"hello"|"hi":
        print("buenos dias" )
    case "Adios"|"bye":
        print("Hasta luego")
    case _ :
        print("No es un mensaje valido")