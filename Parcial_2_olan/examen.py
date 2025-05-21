def actividades(promedio_str):
    with open("actividades.txt"):
        leer= act.readlines()
        return leer

def contraseña_valida(contraseña):
    if (len(contraseña) >= 8 and
        any(contra.isupper() for contra in contraseña) and
        any(contra.isdigit() for contra in contraseña)):
        return "esta contraas es fuerte☠️ "
    return "te pueden hackear bien ficilito bro🥺🥺🥺"

with open("actividades.txt") as act:
    lin= act.readlines()

with open("actividades.txt") as fin:
    for linea in lin:
        try:
            nombre, activi, clavee= linea.strip().split ("|")
            actividad= actividades(print())
            segurida= contraseña_valida(clavee)
            fin.write (f"Nombre {nombre.capitalize()}-Actividades{actividades}-Contraseña{segurida}\n")

        except Exception as error:
            "error en linea"
