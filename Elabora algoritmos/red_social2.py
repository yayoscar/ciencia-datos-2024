print("Bienvenido a...")
print('''
_____________________________    ________  ___________
\______   \_   _____/\______ \   \______ \ \_   _____/
 |       _/|    __)_  |    |  \   |    |  \ |    __)_ 
 |    |   \|        \ |    `   \  |    `   \|        \
 |____|_  /_______  //_______  / /_______  /_______  /
     
   _____      _____  .___  ________ ________    _________
  /  _  \    /     \ |   |/  _____/ \_____  \  /   _____/
 /  /_\  \  /  \ /  \|   /   \  ___  /   |   \ \_____  \ 
/    |    \/    Y    \   \    \_\  \/    |    \/        \
\____|__  /\____|__  /___|\______  /\_______  /_______  /         
''')

nombre = input("Para empezar, dime, ¿cómo te llamas? ")
print()
print("Hola", nombre, ", bienvenido a Mi Red")
print()

agno = int(input("Para preparar tu perfil, dime, ¿en qué año naciste? "))
edad = 2025 - agno - 1
print()

estatura = float(input("Cuéntame más de ti, para agregarlo a tu perfil ¿Cuánto mides? Dámelo en metros: "))
estatura_m = int(estatura)
estatura_cm = int((estatura - estatura_m) * 100)
num_amigos = int(input("Muy bien,  cuéntame, ¿cuántos amigos tienes? "))
print()

telefono = input("Ingrese su número de teléfono: ")
direccion = input("Ingrese su dirección: ")
pais = input("Ingrese su país: ")
sexo = input("Ingrese su sexo (Masculino/Femenino/Otro): ")
ciudad = input("Ingrese su ciudad: ")
print()

print("Muy bien, ", nombre, ". Entonces podemos crear un perfil con estos datos. " )
print("---------------------------------------------------")
print("nombre: ", nombre)
print("Edad: ", edad, "Años")
print("Estatura: ", estatura_m, "metros y", estatura_cm, "centímetros")
print("Amigos: ", num_amigos)
print("Teléfono:", telefono)
print(f"Dirección: ", direccion)
print(f"País: ", pais)
print(f"Sexo: ", sexo)
print(f"Ciudad: ", ciudad)
print("---------------------------------------------------")
print("Gracias por la información. Esperamos que disfrutes con Mi red")
print()

# Menú interactivo
continuar = True
while continuar:
    print()
    print("¿Qué deseas hacer ahora?")
    print("1. Escribir un mensaje")
    print("2. Modificar tu nombre")
    print("3. Ver tu perfil")
    print("N. Salir")
    opcion = input("Selecciona una opción (1/2/3/N): ")

    if opcion == "1":
        mensaje = input("¿Qué piensas hoy? ")
        print()
        print("--------------------------------------------------")
        print(nombre, "dice:", mensaje)
        print("--------------------------------------------------")
    elif opcion == "2":
        nuevo_nombre = input("Escribe tu nuevo nombre: ")
        if nuevo_nombre.strip() != "":
            nombre = nuevo_nombre
            print("Tu nombre ha sido actualizado con éxito.")
        else:
            print("El nombre no puede estar vacío.")
    elif opcion == "3":
        print("--------------------------------------------------")
        print("Nombre: ", nombre)
        print("Edad: ", edad, "años")
        print("Estatura: ", estatura_m, "metros y", estatura_cm, "centímetros")
        print("Amigos: ", num_amigos)
        print(f"Teléfono: {telefono}")
        print(f"Sexo: {sexo}")
        print(f"Dirección: {direccion}")
        print(f"Ciudad: {ciudad}")
        print(f"País: {pais}")
        print("--------------------------------------------------")
    elif opcion == "N" or opcion == "n":
        continuar = False
        print("Gracias por usar Mi Red. ¡Hasta pronto!")
    else:
        print("Opción no válida. Por favor, selecciona una opción del menú.")
