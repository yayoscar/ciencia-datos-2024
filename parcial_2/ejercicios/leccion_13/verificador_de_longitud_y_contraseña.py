def verificador_contrasenia(clave):
    if len(clave)>= 8:
        return True
    return False
print(verificador_contrasenia("lrgeergth"))