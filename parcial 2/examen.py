import re

def validar_contraseña(contrasena):
 if len(contrasena) < 8 or not re.search("[A-Z]", contrasena) or not re.search("[0-9]", contrasena):
   return False, "Contraseña debil."

def main():
    while True:
        contrasena = input("Ingresa una contrasea: ")
        valido, mensaje = validar_contraseña(contrasena)
        print(mensaje)
        if valido:
            break
        else:
            respuesta = input("¿Quieres intentar de nuevo? (s/n): ")
            if respuesta.lower() != "s":
                break

if __name__== "__main__":
    main()
with open("actividades.txt", "r", encoding="utf-8") as actividades:
    actividades.read
print("Aqui esta lo que estaba en el archivo")
with open("actividades.txt", "r", encoding="utf-8") as actividades:
    contenido = actividades.read()
    print(contenido)

