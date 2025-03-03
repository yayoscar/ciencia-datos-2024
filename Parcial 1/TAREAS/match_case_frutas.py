fruta = input("ingresa el nombre de la fruta del cual desea saber su categoría: ")
match fruta:
    case "manzana":
        print("La manzana pertenece a la categoría de las frutas de piel lisa")
    case "naranja":
        print("La naranja pertenece a la categoría de las frutas cítricas")
    case "sandía":
        print("La sandía pertenece a la categoría de las frutas grandes")
    case "pera":
        print("La pera pertenece a la categoría de las frutas de piel lisa")
    case "limón":
        print("El limón pertenece a la categoría de las frutas cítricas")
    case "melón":
        print("El melón pertenece a la categoría de las frutas grandes")
    case "durazno":
        print("El durazno pertenece a la categoría de las frutas de piel lisa")
    case "mandarina":
        print("La mandarina pertenece a la categoría de las frutas cítricas")
    case get:
        print("Esta fruta pertenece a una categoría desconocida")