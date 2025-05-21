def validar_contrasena(contrasena):
    return "Fuerte" if len(contrasena) >= 8 and any(c.isupper() for c in contrasena) and any(c.isdigit() for c in contrasena) else "Débil"

def procesar_actividad(nombre, actividad, duracion, contrasena):
    return f"{nombre.capitalize()}: realizó {actividad} por {duracion} minutos - Contraseña: {validar_contrasena(contrasena)}"

def main():
    with open("actividades.txt", "a") as archivo:
        while True:
            nombre = input("Ingrese su nombre: ")
            actividad = input("Ingrese la actividad realizada: ")
            duracion = input("Ingrese la duración en minutos: ")
            contrasena = input("Ingrese su contraseña: ")
            resultado = procesar_actividad(nombre, actividad, duracion, contrasena)
            print(resultado)
            archivo.write(f"{nombre}|{actividad}|{duracion}|{contrasena}\n")
            respuesta = input("¿Desea ingresar otra actividad? (s/n): ")
            if respuesta.lower() != "s":
                break

    print("\nActividades registradas:")
    with open("actividades.txt", "r") as archivo:
        for linea in archivo:
            if linea.strip():
                nombre, actividad, duracion, contrasena = linea.strip().split('|')
                print(procesar_actividad(nombre, actividad, duracion, contrasena))

if __name__ == "__main__":
    main()


