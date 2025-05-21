def verificar_longitud_de_la_contrasena(clave):
    if len(clave) >8:
        return True
    else:
        return False

print(verificar_longitud_de_la_contrasena("clave683dwd"))