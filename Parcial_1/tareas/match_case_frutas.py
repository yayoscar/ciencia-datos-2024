fruta = input("Ingresa el nombre de una fruta: ")

match fruta:
    case "Manzana":
        print ("Manzana")
    case"Pera":
        print ("Pera")

    case "Platano":
        print ("Platano")

    case "Mango":
     print("Mango")

    case "Melon":
        print ("Melon")
    case "Sandia":
        print ("Sandia")
    case _:
        print("Esa no es una fruta")
