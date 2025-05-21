mensaje = "ingrese un pais: "
while True:
    pais=input("indica en que idioma quieres saludar alemania/italia/mexico: ")
    match pais:
        case "alemania":
            print("hallo")
        case "italia":
            print("ciao")
        case "mexico":
            print("hola")