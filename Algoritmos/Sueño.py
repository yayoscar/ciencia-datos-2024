Horas = input("¿Cuántas horas duermes al dia?: ")
match Horas:
    case "1 hora" | "2 horas" | "3 horas":
        print("Tus horas de sueño son extremadamente bajas, a continuación te estaré mostrando algunos números telefónicos de profesionales e instituciones para que usted puedo consultar y lo puedan ayudar ")
        print()
        print("INSTITUCIONES:")
        print("Secretaría de salud de México (55 5062 1600)")
        print("Unidad de Trastornos del Movimiento y Sueño (55 6841 3746)")
        print("Hospital general ajusco medio en CDMX (55 7693 9104)")

        print("NÚMERO DE PROFESIONALES:")
        print("Psiquitra Armando: 986 874 2748")
        print("Neurólogo Jacinto: 983 112 4673")
        print("Doctora Vianney: 983 700 4749")

    case "4 horas" | "5 horas" | "6 horas":
        print("No estas durmiendo correctamente, a continuación te estaré dejando algunos consejos que tal vez sean de utilidad ")
        print()
        print("1-Establece un buen horario de sueño")
        print("2-Crea una rutina de relajación antes de dormir")
        print("2-Evita la cafeína y el alcohol antes de dormir ")
        print("4-Realiza actividad física regular")
        print("5-Evita comer una comida pesada antes de dormir ")
        print("6-Evita el uso de dispositivos móviles antes de dormir")

    case "7 horas" | "8 horas" | "9 horas" | "10 horas":
        print("QUE BIENNN, Tienes un buen hàbito de sueño, FELICIDADES SEGUE ASÍ")