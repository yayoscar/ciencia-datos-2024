def validar_contraseña(contraseña="actividades.txt"):
    longitud=False
    if len(contraseña) >= 8:
       longitud=True

    mayuscula=False
    for partes in contraseña:
        if partes.isupper():
            mayuscula=True

    numero =False
    for partesitas in contraseña:
        if partesitas.isdigit():
            numero=True
    if longitud and mayuscula and numero ==True:
       respuesta= print("la contraseña es fuerte")
    else:
       respuesta= print("la contraseña es debil")
    return respuesta


def formatear_lineas():
    with open("actividades.txt","r") as archivo:
        return





print(validar_contraseña())
#no supe como se dividie el archivo intente con un split y no lo hacia
























