print("Bienvenido a...")
print("""
___________.__   
\_   _____/|  |  
 |    __)_ |  |  
 |        \|  |__
/_______  /|____/
        \/       
_________                        __                             
\_   ___ \_______ __ __  _______/  |______    ____  ____  ____  
/    \  \/\_  __ \  |  \/  ___/\   __\__  \ _/ ___\/ __ \/  _ \ 
\     \____|  | \/  |  /\___ \  |  |  / __ \\  \__\  ___(  <_> )
 \______  /|__|  |____//____  > |__| (____  /\___  >___  >____/ 
        \/                  \/            \/     \/    \/       
_________                                             .___                     
\_   ___ \_____    ______ ____ _____ _______ __ __  __| _/______  _  _______   
/    \  \/\__  \  /  ___// ___\\__  \\_  __ \  |  \/ __ |/  _ \ \/ \/ /\__  \  
\     \____/ __ \_\___ \\  \___ / __ \|  | \/  |  / /_/ (  <_> )     /  / __ \_
 \______  (____  /____  >\___  >____  /__|  |____/\____ |\____/ \/\_/  (____  /
        \/     \/     \/     \/     \/                 \/                   \/ 
""")

nombre = input("Para empezar, dime como te llamas")
print()
print("Hola", nombre, ", bienvenido a El Crustaceo Cascarurdo")
print()
agno =int(input("Para preparar tu perfil, dime en que año naciste."))
edad = 2025-agno-1
print()
estatura = float(input("Cuéntame más de ti, para agregarlo a tu perfil. ¿Cuánto mides? Dámelo en metros. "))
estatura_m = int(estatura)
estatura_cm = int( (estatura - estatura_m)*100)
edad = int(input("¿Y cuántos años tienes?"))
telefono = int(input("¿Cuál es tu numero de telefono?"))
sexo = (input("Dime, ¿Cuál es tu sexo?"))
ciudad = (input("Fantástico, dime, ¿En qué ciudad vives?"))
pais_nacim = (input("Y cuéntame, ¿En qué pais nacíste?"))
direccion = (input("Eso es genial, ¿Dónde vives? Dame tu direccion."))
num_amigos = int(input("Muy bien. Finalmente, ¿Cuántos amigos tienes?"))
print()
print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
print("--------------------------------------------------")
print("Nombre:  ", nombre)
print("Edad:  ", edad, "años")
print("Año de nacimeinto: ", agno)
print("Estatura:", estatura_m, "metros y ", estatura_cm, "centímetros")
print("Telefono: ", telefono)
print("Sexo: ", sexo)
print("Ciudad: ", ciudad)
print("Pais de nacimiento: ", pais_nacim)
print("Dirección: ", direccion)
print("Amigos:  ", num_amigos)
print("---------------------------------------------------")
respuesta = input("Si no està conforme con su nombre, lo puede cambiar, ¿Le gustarìa cambiarlo? (S/N)")
if respuesta == "S" or respuesta == "s":
   nuevo_nombre=input("¿Cuàl quiere que sea su nuevo nombre?")
print("Su nuevo nombre es ", nuevo_nombre, ".")
print("Esta es su nueva ficha de datos.")
print("--------------------------------------------------")
print("Nombre:  ", nuevo_nombre)
print("Edad:  ", edad, "años")
print("Año de nacimeinto: ", agno)
print("Estatura:", estatura_m, "metros y ", estatura_cm, "centímetros")
print("Telefono: ", telefono)
print("Sexo: ", sexo)
print("Ciudad: ", ciudad)
print("Pais de nacimiento: ", pais_nacim)
print("Dirección: ", direccion)
print("Amigos:  ", num_amigos)
print("---------------------------------------------------")
print("Gracias por la información. Esperamos que disfrutes de la experiencia ofrecida en El Crustacio Cascarudo")
print()
continuar = True
while continuar:
    escribir_mensaje = str(input("¿Deseas escribir un mensaje? (S/N)"))

    if escribir_mensaje == "S" or escribir_mensaje == "s" or escribir_mensaje == "":
        mensaje = input("Vamos a publicar un mensaje. ¿Que piensas hoy?")
        print()
        print("-------------------------------------------------")
        print(nuevo_nombre, "dice: ", mensaje)
        print("-------------------------------------------------")
    elif escribir_mensaje == "N" or escribir_mensaje == "n":
        continuar = False
    else:
        print("No entiendo lo que quieres decir.")
continuar = False
print("Gracias por usar El Crustaceo Cascarudo. ¡Hasta pronto!")


