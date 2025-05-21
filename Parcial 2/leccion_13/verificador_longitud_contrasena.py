def password(clave):
    if len(clave) <= 8 :
        return False
    return True

print(password("clavesuperipermegasegura"))