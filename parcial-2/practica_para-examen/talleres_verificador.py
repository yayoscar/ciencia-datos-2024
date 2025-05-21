def calcular_asistencia(lista_asistencias):
    total = len(lista_asistencias)
    if total == 0:
        return 0
    return (sum(lista_asistencias) / total) * 100


def validar_correo(correo):
    if "@" in correo:
        dominio = correo.split("@")
        if len(dominio) > 1 and "." in dominio[1]:
            return True
    return False


with open ("talleres.txt","r") as talleres_archivo, open("talleres_procesados.txt","w") as archivo_procesado:
    for usuarios in talleres_archivo:
        partes = usuarios.split("|")
        nombre = partes[0]
        correo_usuario = partes[1]
        asistencias_str = partes[2]

        asistencias_usuario = [int(n) for n in asistencias_str.strip().split(",")]
        asistencias_usuario_funcion = calcular_asistencia(asistencias_usuario)
        correo_usuario_funcion = "valido" if validar_correo(correo_usuario) else "invalido"

        archivo_procesado.write(f"Nombre: {nombre} Asistencia: {asistencias_usuario_funcion:.2f}% Correo: {correo_usuario_funcion}\n ")