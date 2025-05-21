with open("actividades.txt","r") as archivo:
    lineas = archivo.readlines()

    for linea in lineas:
        nombres, actividades, duraciones, contrasenas = linea.strip().split("-")

def lista_nombres(lista_nombres):
    nombres =[any(nombre)for nombre in lista_nombres.split("-")]
    return lista_nombres


def lista_actividades(actividad):
    actividad=[float(actividad) for actividad in lista_actividades.split("-")]
    return actividad


def lista_duraciones(duracion):
    duracion =[float(duracion) for duracion in lista_duraciones.split("-")]
    return duracion


def validar_contrasena(contrasenas):
    es_larga = len(contrasenas) >= 8
    tiene_mayuscula = any(c.isupper()for c in contrasenas)
    tiene_numero = any(c.isdigit()for c in contrasenas)
    return "Fuerte" if es_larga and tiene_mayuscula and tiene_numero else "Débil"


seguridad_contrasena = validar_contrasena(contrasenas)

for linea in lineas:
        nombres, actividades, duraciones, contrasenas = linea.strip().split("-")
        nombre = nombres
        actividad = actividades
        duracion = duraciones
        seguridad_contrasena = validar_contrasena(contrasenas)

print(f"Nombre: {nombre.capitalize()} - realizo: {actividad} - por: {duracion} minutos - Contraseña segura: {seguridad_contrasena}\n")
