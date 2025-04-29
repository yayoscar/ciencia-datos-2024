print("bienvenido a ...")
print(""" )  ____) |  |   |  | |        | |        | \    ___) |    \  
(  (___   |  |   |  | |  |\/|  | |  |\/|  |  |  (__   |     ) 
 \___  \  |  |   |  | |  |  |  | |  |  |  |  |   __)  |    /  
 ____)  ) |   \_/   | |  |  |  | |  |  |  |  |  (___  | |\ \  
(      (___\       /__|  |__|  |_|  |__|  |_/       )_| |_\ \_
_       ______  _____     ___     ___    _        ___       ___       __
 )  ____)    /  \    |    \  |    \  |  | \    ___)  )  ____)  )  ____) 
(  (___     /    \   |     | |  |\ \ |  |  |  (__   (  (___   (  (___   
 \___  \   /  ()  \  |     | |  | \ \|  |  |   __)   \___  \   \___  \  
 ____)  ) |   __   | |     | |  |  \    |  |  (___   ____)  )  ____)  ) 
(      (__|  (__)  |_|    /__|  |___\   |_/       )_(      (__(      (__
""")
nombre = input("para empezar, dime como te llamas. ")
print()
print("Hola", nombre, ", bienvenido a summer sadness")
print()
agno = int(input("para preparar tu perfil, dime en que año naciste. "))
edad = 2025-agno-1
print()


estatura = float (input("cuentame más de ti, para agrgarlo a tu perfil. ¿cuanto mides? Dámelo en metros. "))
estatura_m = int(estatura)
estatura_cm = int( (estatura - estatura_m)*100)
sexo = (input("dime;¿cual es tu sexo?"))
print()
ciudad = str(input("¿En que ciudad vives?"))
print()
telefono = int(input("¿Cual es tu numero de telefono?"))
print()
direccion = input("¿cual es tu direccion?")
print()
num_amigos = int(input("muy bien finalmente, ¿cuantos amigos tienes?"))
print()
print("muy bien,",nombre,". Entonces podemos crear un perfil con estos datos.")
print("______________________")
print("Nombre: ", nombre)
print("edad:  ", edad, "años")
print("año de nacimiento")
print("estatura:",estatura_m, "metros y",estatura_cm, "centimetros")
print("sexo:", sexo)
print("ciudad", ciudad)
print("telefono", telefono)
print("amigos: ",num_amigos)
print("____________________________")
respuesta = input("si no está satisfecho con su nombre, puede cambiarlo, ¿desea cambiarlo? (N/S")
if respuesta == "S" or respuesta == "s":
    Nuevo_nombre=input("¿cual quiere que sea su nuevo nombre?")
print(("Su nuevo nombre es ", Nuevo_nombre, "."))
print("Esta es su nueva ficha de datos.")
print("________________________________")
print("nombre: ", Nuevo_nombre)
print("Gracias por la informacion. esperamos que disfrutes con mi red")
print()
continuar = True
while continuar:
    escribir_mensaje = str(input("¿Deseas escribir un mensaje? (S/N"))
    if escribir_mensaje == "S" or escribir_mensaje == "s" or escribir_mensaje == "":
        mensaje = input("vamos a publicar un mensaje. ¿Qué piensas hoy? ")
        print()
        print("______________________________________________________")
        print(nombre, "dice:",mensaje)
        print("_______________________________________________________")

    else:
        continuar = False
        print("Gracias por usar Summer sadness. ¡Hasta pronto!")




