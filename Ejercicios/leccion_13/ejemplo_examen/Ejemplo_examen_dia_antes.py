with open("reporte.txt","r") as archivo:
    lineas=archivo.readlines()

    for linea in lineas:
        nombre, notas, contrasena = linea.strip().split("|")

def calcular_promedio(lista_notas):
    notas=[float(nota) for nota in lista_notas.split(",")]
    return sum(notas) / len(notas)

promedio = calcular_promedio(notas)


def validar_contrasena(contrasena):
    es_larga = len(contrasena) >= 8
    tiene_mayuscula = any(c.isupper()for c in contrasena)
    tiene_numero = any(c.isdigit()for c in contrasena)
    return "Fuerte" if es_larga and tiene_mayuscula and tiene_numero else "Débil"


seguridad_contrasena = validar_contrasena(contrasena)

with open("reporte_valido.txt","w") as archivo_salida:
    for linea in lineas:
        nombrs, notas, contrasena = linea.strip().split("|")
        promedio = calcular_promedio(notas)
        seguridad_contrasena = validar_contrasena(contrasena)
        archivo_salida.write(f"Nombre: {nombre} - Promedio: {promedio:.2f} - Contraseña segura: {seguridad_contrasena}\n")
