def calcular_promedio(notas):
    notas = (float(nota) for nota in notas.split(","))
    return round(sum(notas)/len(notas),2)

def validar_contraseña(contraseña):

    if len(contraseña)>=8 and any(c.i
