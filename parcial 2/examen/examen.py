with (open("actividades.txt","r") as archivo):
    contenido = archivo.read()
    print(contenido)

    import re
    error = []

    password = input("ingrese una contraseña")
    largo = len(password)
    if largo >8:
        print("tu contraseña es buena")
    if len(password) <7:
        print("la contraseña no es segura")
    if not re.search("[a-z]",password) or not re.search("[A-Z]", password):
        error.append("La contrasena debe de tener letras mayusculas y minusculas")
    if not re.search("[0-9]", password):
        error.append("La contrasena debe de tener al menos 1 numero")

with open("examen.py","r") as archivo:
    lineas = archivo.readlines()
print(f"el archivo tiene{len(lineas)} lineas.")
