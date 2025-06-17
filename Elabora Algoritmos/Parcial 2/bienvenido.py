print("Bienvenido a...")
print( '''
 __________            .__  
 \____    /__ _________|__|   
     /     /|  |  \_  __ \  |  
    /     /_|  |  /|  | \/  | 
   /_______ \____/ |__|  |__|         
           \/      
''')

nombre = input("Para empezar, dime, ¿cómo te llamas? ")
print()
print("Hola", nombre, ", bienvenido a Mi Red")
print()

agno = int(input("Para preparar tu perfil, dime, ¿en qué año naciste? "))
edad = 2025 - agno - 1
print()

estatura = float(input("Cuéntame más de ti, para agregarlo a tu perfil ¿Cuánto mides? Dámelo en metros "))
estatura_m = int(estatura)
estatura_cm = int((estatura - estatura_m) * 100)
num_amigos = int(input("Muy bien. Finalmente, cuéntame, ¿cuántos amigos tienes? "))
print()

print("Muy bien,", nombre, ", entonces podemos crear un perfil con estos datos")
print("--------------------------------------------------")
print("Nombre: ", nombre)
print("Edad: ", edad, "años")
print("Estatura: ", estatura_m, "metros y", estatura_cm, "centímetros")
print("Amigos: ", num_amigos)
print("--------------------------------------------------")
print("Gracias por la información. Esperamos que disfrutes con Mi Red.")
print()

telefono = input("Ingrese su número de teléfono: ")
sexo = input("Ingrese su sexo (M/F): ")
direccion = input("Ingrese su dirección: ")
ciudad = input("Ingrese su ciudad: ")
pais = input("Ingrese su país: ")
print("--------------------------------------------------")
print("Datos ingresados: ")
print(f"Teléfono: {telefono}")
print(f"Sexo: {sexo}")
print(f"Dirección: {direccion}")
print(f"Ciudad: {ciudad}")
print(f"País: {pais}")
print("--------------------------------------------------")

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
        nombre = input("Escribe tu nuevo nombre: ")
        print("Tu nombre ha sido actualizado con éxito.")
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