print("Bienvenido a... ")
print("""
_____________________________    ________  ___________
\______   \_   _____/\______ \   \______ \ \_   _____/
 |       _/|    __)_  |    |  \   |    |  \ |    __)_ 
 |    |   \|        \ |    `   \  |    `   \|        \
 |____|_  /_______  //_______  / /_______  /_______  /
        \/        \/         \/          \/        \/ 
   _____      _____  .___  ________ ________    _________
  /  _  \    /     \ |   |/  _____/ \_____  \  /   _____/
 /  /_\  \  /  \ /  \|   /   \  ___  /   |   \ \_____  \ 
/    |    \/    Y    \   \    \_\  \/    |    \/        \
\____|__  /\____|__  /___|\______  /\_______  /_______  /
        \/         \/            \/         \/        \/ 
 """)


nombre= input("Para empezar, dime cómo te llamas. ")
print()
print("Hola", nombre, ", bienvenido a Mi red")
print()

agno= int(input("Para preparar tu perfil, dime en qué año naciste. "))
edad= 2025-agno-1
print()

estatura = float(input("Cuéntame más de ti, para agregarlo a tu perfil. ¿Cuánto mides? Dámelo en metros. "))
estatura_m = int(estatura)
estatura_cm = int((estatura-estatura_m)*100)

num_amigos = int(input("Muy bien. finalmente, cuéntame cuántos amigos tienes."))

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

continuar = True
while continuar:
    opcion = input("¿Deseas escribir un mensaje? (S/N): ")
    if opcion == "S" or opcion == "s":
        mensaje = input("Vamos a publicar un mensaje. ¿Qué piensas hoy? ")
        print()
        print("_____________________________________________")
        print(nombre, "dice:", mensaje)
        print("_____________________________________________")
        print()
    elif opcion == "N" or opcion == "n":
        continuar = False
    else:
        print("Opción no válida. Por favor, responde solo con 'S' o 'N'.")
        print()

print("Gracias por usar Mi red. ¡Hasta pronto!")

