def hacer_pregunta(respuesta):
    match respuesta:
        case "bien":
            print("¡Qué bueno!")
        case "mal":
            print("¡Qué mal!")
        case _:
            print("No entendí tu respuesta")


def hacer_pregunta_2(respuesta2):
    match respuesta2:
        case _:
            print("¡Ñaaaam, que rico!")

def hacer_pregunta_3(respuesta3):
    print(f"Tu cumpleaños es el {respuesta3}. ¡Habrá que celebrarlo!")


def hacer_pregunta_4(respuesta4):
    print(f"¡Oh, me encanta {respuesta4} también!")


respuesta = input("¿Cómo estás?: ").strip().lower()
hacer_pregunta(respuesta)

respuesta2 = input("¿Qué desayunaste?: ").strip().lower()
hacer_pregunta_2(respuesta2)

respuesta3 = input("¿Cuándo es tu cumpleaños?: ").strip()
hacer_pregunta_3(respuesta3)

respuesta4 = input("¿Cuál es tu bebida favorita?: ").strip().lower()
hacer_pregunta_4(respuesta4)
#Daniela Beatriz Chin Morales