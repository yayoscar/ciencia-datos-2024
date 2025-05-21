def calcular_promedio(lista_numeros):
    calculo = sum(lista_numeros) / len(lista_numeros)
    return calculo

def validar_matricula(matricula):
    caracteres = len(matricula)==9
    mayus = matricula[0].isupper()
    numeros = matricula[1:].isdigit()
    return caracteres and mayus and numeros


with open("accesos.txt","r") as accesos_archivo, open("accesos_procesados.txt","w") as accesos_nuevos:
    for usuarios in accesos_archivo:
        partes = usuarios.strip().split("|")
        nombres = partes[0]
        matricula_usuario = partes[1]
        libros_solicitados_str = partes[2]

        libros_solicitados = [int(n) for n in libros_solicitados_str.split(",")]
        estado_de_matricula = "valida" if validar_matricula(matricula_usuario) else "invalida"

        accesos_nuevos.write(f"Nombre: {nombres} - Promedio libros: {libros_solicitados} Estado de matricula: {estado_de_matricula}\n")