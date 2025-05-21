def validar_telefono(telefono):
    digitos = len(telefono)
    if digitos == 10:
        if telefono.isdigit():
            return True
    return False


def calcular_asistencia(lista_asistencias):
    calculo = sum(lista_asistencias)/len(lista_asistencias)*100
    return calculo

with open("conferencias.txt", "r") as conferencia_archivo, open("conferencias_procesadas.txt","w") as actualizado_conferencia_archivo:
    for usuario in conferencia_archivo:
        partes = usuario.strip().split("|")
        nombre_usuario = partes[0]
        telefono_usuario = partes[1]
        asistencia_str = partes[2]

        validar_funcion = "valido" if validar_telefono(telefono_usuario) else "invalido"
        asistencia_int = [int(n) for n in asistencia_str.strip().split(",")]
        asistencia_funcion = calcular_asistencia(asistencia_int)

        actualizado_conferencia_archivo.write(f"Nombre: {nombre_usuario} Telefono: {validar_funcion} Asistencia: {asistencia_funcion:.2f}%\n")