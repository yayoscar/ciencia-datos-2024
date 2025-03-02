while True:
    pais=input("ingrese un pais italia/alemania/mexico: ")
    match pais:
        case "mexico":
            print("hola")
        case "alemania":
            print("hallo")
        case "italia":
            print("ciao")