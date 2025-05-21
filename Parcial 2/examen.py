def validar_contraseña(contraseña):
    tiene_mayuscula = any(c.isupper() for c in contraseña)
    tiene_numero = any(c.isdigit() for c in contraseña)
    longitud_valida = len(contraseña) >= 8

    return longitud_valida and tiene_mayuscula and tiene_numero

def procesar_actividades(ruta_archivo):
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                partes = linea.strip().split(',')

                if len(partes) != 3:
                    print("Línea con formato correcto:", linea)
                    continue

                nombre, actividad, duracion, contraseña = partes
                nombre_capitalizado = nombre.strip().capitalize()
                actividad = actividad.strip()
                duracion = duracion.strip()
                contraseña = contraseña.strip()

                fortaleza = "Fuerte" if validar_contraseña(contraseña) else "Débil"

                print(f"{nombre_capitalizado}: realizó {actividad} por {duracion} minutos - contraseña {fortaleza}")
    except FileNotFoundError:
        print("No se encontró el archivo:", ruta_archivo)

# Ejecutar el programa
procesar_actividades("actividades.txt")
