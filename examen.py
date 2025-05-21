nombre=input("Ingresa tu nombre.")
actividad=input("Ingresa tu actividad favorita.")
tiempo=input("¿Cuánto tiempo al día haces esa actividad?")

def contraseña_segura(contraseña):
    largo=False
    may=False
    numm=False
    if len(contraseña) >= 8:
       largo=True
    for i in range(len(contraseña)):
        if contraseña[i].isupper():
            may=True
        if contraseña[i].isnumeric():
            num=True

    if largo and may and num == True:
        return True
    else:
        return False

contraseña=input("Ingresa una contraseña: ")
verificar=contraseña_segura(contraseña)
if verificar==True:
    print ("La contraseña es fuerte.")
else:
    print("La contraseña es débil")

print(["Nombre:",nombre])
print(["Realizo:", actividad])
print(["Duración:", tiempo])
print(["Contraseña:",contraseña])

try:
    with open("actividades.txt", "r") as archivo:
        texto = archivo.read()
        palabra = input("Introduce una palabra: ")
        cuenta = texto.lower().count(palabra.lower())
        
except FileNotFoundError:
    print("El archivo 'actividades.txt' no se encontró.")

