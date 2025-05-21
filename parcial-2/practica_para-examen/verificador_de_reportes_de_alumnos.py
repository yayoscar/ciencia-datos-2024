def calcular_promedio(lista_notas):
    calculo = sum(lista_notas) / len(lista_notas)
    return calculo

def validar_contrasena(contraseña):
    lon =len(contraseña) >= 8
    may = any(c.isupper() for c in contraseña)
    digit = any(d.isdigit() for d in contraseña)
    return lon and may and digit

with open("reporte.txt", "r") as reporte, open("reporte_valido.txt", "w") as reporte_nuevo:
    for linea in reporte:
        partes = linea.strip().split("|")
        nombre =partes[0]
        calificaciones_texto = partes[1]
        contrasena = partes[2]

        calificaciones = [float(n) for n in calificaciones_texto.split(',')]
        reporte_nuevo.write(
            f"Nombre: {nombre} - Promedio: {calcular_promedio(calificaciones):.2f} - Contraseña: {'fuerte' if validar_contrasena(contrasena) else 'debil'}\n")
