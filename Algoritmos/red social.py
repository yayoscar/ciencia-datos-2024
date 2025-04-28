from operator import truediv

print("Bienvenido a ... ")
print("""

(  ____ \(  ___  )(  ____ \\__   __/( (    /|(  ___  )
| (    \/| (   ) || (    \/   ) (   |  \  ( || (   ) |
| |      | |   | || |         | |   |   \ | || (___) |
| |      | |   | || |         | |   | (\ \) ||  ___  |
| |      | |   | || |         | |   | | \   || (   ) |
| (____/\| (___) || (____/\___) (___| )  \  || )   ( |
(_______/(_______)(_______/\_______/|/    )_)|/     \|
                                      
""")
nombre = input("Para empezar, dime como te llamas. ")
print()
print("Hola ",nombre, ", bienvenidoa Mi Red")
print()
agno = int(input("Para empezar tu perfil, dime en que año naciste. "))
edad = 2025-agno-1
print()
estatura = float(input("Cuentame más de ti, para agregarlo a tu perfil, ¿Cuánto mides? Dámelo en metros. "))
estatura_m = int(estatura)
estatura_cm = int( (estatura - estatura_m)*100 )
num_amigos = int(input("Muy bien. Finalmente, cuéntame cuantos amigos tienes. "))
print()
print("Muy bien,", nombre, ".Entonces podemos crear un perfil con estos datos.")
print("---------------------------------------------------")
print("Nombre: ", nombre)
print("Edad: ", edad, "años")
print("Estatura: ", estatura_m, "metros y", estatura_cm, "centimetros")
print("Amigos: ", num_amigos)
print("---------------------------------------------------------------------------")
respuesta = input("si no esta conforme con su nombre lo puede cambiar ¿le gustaria camniarlo? (S/N)")
if respuesta == "S" or "s":
    nuevo_nombre=input("¿Cuál es su nuevo nombre?")
    print("Su nuevo nombre es ", nuevo_nombre, ".")
    print("Esta es su nueva ficha de datos")
print("Gracias por la información. Esperamos que disfrutes con Mi Red")
print()
print("--------------------------------------------------------------------------")
sexo = str(input("Ingrese su sexo"))
print()
numero_de_telefono = str (input("Ingrese su número de telefono"))
print()
ciudad_donde_vive = str(input("Ingrese el nombre de la ciudad donde vive"))
print()
pais_de_nacimiento = str(input("Ingrese el nombre de su país de nacimiento"))
print()
direccion = str(input("Ingrese su dirección"))
print()
print("--------------------------------------------------------------------------")
print("Sexo: ", sexo)
print("numero de telefono:",numero_de_telefono)
print("País de nacimiento: ", pais_de_nacimiento)
print("Dirección:", direccion)
print("--------------------------------------------------------------------------")
print("Gracias por tu información, espero que disfrutes Mi Red")
print()
continuar = True
while continuar:
    escribir_mensaje = str (input("¿Deseas escribir un mensaje? (S/N) "))
    if escribir_mensaje == "S" or escribir_mensaje == "s" or escribir_mensaje =="":
       mensaje = input("Vamos a publicar un mensaje . ¿Qué piensas hoy? ")
       print()
       print("--------------------------------------------------------------------------")
       print(nuevo_nombre,"dice",mensaje)
       print("--------------------------------------------------------------------------")
    elif escribir_mensaje == "N" or escribir_mensaje == "n":
        continuar = False
else:
  print("La opcion que ingreso es invalida.")
continuar = False
print("Gracias por usar mi red. Hasta pronto")

