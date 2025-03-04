dia =input("ingrese un dia de la semana(en minusculas): ")
match dia:
    case "lunes":
        print("inicio de semana")
    case "miercoles":
        print("mitad de semana")
    case "sabado"| "domingo":
        print("es fin de semana")
    case "martes"| "jueves"| "viernes":
        print("Dia normal")
    case _:
        print("no es un dia valido")