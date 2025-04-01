while True:
    accion_usuario= input("Coloca una fruta: ")
    match accion_usuario:
        case "Manzana" | "Pera" | "Durazno" :
            print("Es una fruta de piel lisa")
            print( )
            print("Para salir, ingrese salir ")

        case "Naranja" | "Limón" | "Mandarina" :
            print("Es una fruta cítrica")
            print()
            print("Para salir, ingrese salir ")
        case "Sandía" | "Melón" :
            print("Es una frutra grande")
            print()
            print("Para salir, ingrese salir ")
cccc