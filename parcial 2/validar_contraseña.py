# validar_contraseña.py

def fuerza(contraseña):
    """
    Verifica la fuerza de una contraseña.

    Parámetros:
    contraseña (str): La contraseña a verificar.

    Retorna:
    str: "Contraseña Fuerte" si cumple con los requisitos, de lo contrario "Contraseña Débil".
    """
    tiene_longitud = len(contraseña) >= 8
    tiene_mayuscula = any(c.isupper() for c in contraseña)
    tiene_digito = any(c.isdigit() for c in contraseña)

    if tiene_longitud and tiene_mayuscula and tiene_digito:
        return "Contraseña Fuerte"
    else:
        return "Contraseña Débil"
