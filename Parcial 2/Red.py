print("Bienvenido a ... ")
print("""

\__    ___/______ __ __  _____ _____    ____  
  |    |  \_  __ \  |  \/     \\__  \  /    \ 
  |    |   |  | \/  |  /  Y Y  \/ __ \|   |  \
  |____|   |__|  |____/|__|_|  (____  /___|  /
                             \/     \/     \/ 
""")

nombre = input("Para empezar, ¿Dime como te llamas?. ")
print()
print("Hola ", nombre, ", bienvenido a Mi Red")
print()

agno = int(input("Para preparar tu perfil, dime ¿En que año naciste?. "))
edad = 2025-agno-1
print()

estatura = float(input("Cuéntame más de ti, para agregarlo a tu perfil. ¿Cuánto mides? Dámelo en metros. "))
estatura_m = int(estatura)
estatura_cm = int( (estatura - estatura_m)*100 )

sexo = input("Ingrese su sexo (Masculino/Femenino/otro): ")
ciudad = input("Ingrese su ciudad: ")
pais = input("Ingrese su país de origen: ")
direccion = input("Ingrese su dirección: ")
telefono = input("Ingrese su número teléfonico: ")

num_amigos = int(input("Muy bien. Finalmente, cuéntame ¿Cuántos amigos tienes?. "))
print()
print("Muy bien, ", nombre, ". Entonces podemos crear un perfil con estos datos.")
print("---------------------------------------------------")
print("Nombre: ", nombre)
print("Edad: ", edad)
print("Estatura: ", estatura_m, "metros y", estatura_cm, "centimetros")
print("Sexo:", sexo)
print("Ciudad: ", ciudad)
print("País: ", pais)
print("Dirección: ", direccion)
print("Teléfono: ", telefono)
print("Número de amigos: ", num_amigos)
print("---------------------------------------------------")
print("Gracias por la información. Esperemos disfrutes con Mi Red")
print()
continuar = True
#Este ciclo se mantiene en ejucución hasta que el usuario desee salir
while continuar:

    #Solicitamos opción al usuario
 escribir_mensaje = str(input("¿Deseas escribir un mensaje? (S/N) "))

#Vamos a aceptar que el usuario ingrese un mensaje cuando escriba "S","s", o nada
 if escribir_mensaje == "S" or escribir_mensaje == "s" or escribir_mensaje == "":
     mensaje = input("Vamos a publicar un mensaje. ¿Qué piensas hoy? ")
     print ()
     print ("------------------------------------------")
     print (nombre, "dice:", mensaje)
     print ("------------------------------------------")
#En caso que sea otra respuesta, vamos a decidir tu salir.
#en la siguiente interacción del ciclo terminará.
 else:
     continuar = False
 #Mensaje de salida, una vez que el ciclo ha terminado.
 print ("Gracias por usar Mi Red.¡Hasta pronto!" )