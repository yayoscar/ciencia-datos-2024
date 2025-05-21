
archivo=open("archivo.txt","r")
contenido=archivo.readline()
c = input("Ingresa una contraseña, Más de 8 caracteres. "
          " Al menos una letra mayúscula."
          " Al menos un número: ")
if len(c) > 8 and any(x.isupper() for x in c) and any(x.isnumeric() for x in c):
    print("Contraseña FUERTE ✅")
else:
    print("Contraseña DEBIL ❌")