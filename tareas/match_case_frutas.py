fruta = input("ingrese una fruta:")



match (fruta):



    case "naranja"| "limon"| "mandarina":
        print("Fruta citrica")
    case "manzana" | "pera" | "durazno":
        print("Fruta de piel lisa")
    case "papaya" | "melon" | "sandia":
        print("Fruta grande")


    case _:
        print("No es o no ingreso una fruta comentada")
