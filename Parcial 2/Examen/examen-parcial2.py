def nombres():
  nombres = "lisa, carlos, ana"
  nombres.capitalize()
  return nombres


def actividades():
    actividades= "lectura, caminar, estudiar"
    return actividades

def minutos():
    minutos = "30, 45, 60"
    return minutos

def validar_contrasena(contrasena):
    if (len(contrasena) >= 8 and
        any(c.isupper() for c in contrasena) and
        any(c.isdigit() for c in contrasena)):
        return "Fuerte"
    return "Débil"

with open("actividades.txt", "r") as archivo:
    lineas = archivo.readlines()

with open("actividades.txt", "w") as salida:
        for linea in lineas:

             try:
                actividads, minutos, validar_contraseña = linea.strip().split('|')
                actividades = actividades(actividades)
                minutos = minutos(minutos)
                validar_contraseña= validar_contrasena(validar_contraseña)
                salida.write = (f"actividades: {actividades} - minutos: {minutos} - validar_contraseña: {validar_contraseña}\n")
             except Exception as e:
                 salida.write("Error en línea: " + linea)






