# examen.py

def validar_contrasena(clave):
    tiene_mayuscula = any(c.isupper() for c in clave)
    tiene_numero = any(c.isdigit() for c in clave)
    return len(clave) >= 8 and tiene_mayuscula and tiene_numero


def formatear_linea(linea):
    partes = linea.strip().split("|")
    if len(partes) != 4:
        return None  # Error de liena

    usuario, actividad, duracion, clave = partes
    usuario = usuario.capitalize()
    es_fuerte = "Fuerte" if validar_contrasena(clave) else "Débil"

    return f"{usuario}: realizó {actividad} por {duracion} minutos - Contraseña: {es_fuerte}"


def main():
    try:
        with open("actividades.txt", "r") as archivo:
            for linea in archivo:
                resultado = formatear_linea(linea)
                if resultado:
                    print(resultado)
    except FileNotFoundError:
        print("El archivo 'actividades.txt' no se encontró.")


if __name__ == "__main__":
    main()
