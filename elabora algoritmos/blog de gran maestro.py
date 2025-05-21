nombre = input("para empezar,dime como te llamas. ")
print()
print("hola",nombre,",bienvenido a mi red")
print()

agno = int(input("para preparar tu perfil,dime en q año naciste, "))
edad = 2025-agno-1
print()

estatura = float(input("cuentame mas de ti,para agregarlo a tu perfil.¿cuanto mides? damelo es metros."))
estatura_m = int(estatura)
estatura_cm = int((estatura - estatura_m)*100)
telefono = int(input("¿Cuál es tu numero de teléfono?"))
direccion = (input("¿Dónde vives?"))
pais = (input("¿En que pais vives?"))
pais_nacim = (input("¿En qué pais naciste?"))
num_amigos = int(input("muy bien,finalmente,cuentame cuantos amigos tienes."))


print()
print("muy bien,",nombre,",entonces podemos crear un perfil con estos datos.")
print("__________________________________________________")
print("nombre: ",nombre)
print("edad: ",edad,"años")
print("estatura: ",estatura_m,"metros y",estatura_cm,"centimetros")
print("amigos: ",num_amigos)
print("Teléfono: ", telefono)
print("Direccion: ", direccion)
print("Pais: ", pais)
print("País de nacimiento: ", pais_nacim)
print("___________________________________________________")
print("gracias por la informacion.esperamos que disfrutes con mi red")
print()
continuar = True
while continuar:
    escribir_mensaje = str(input("¿deseas finalizar en esta red? (s/n)"))
    if escribir_mensaje == "N" or escribir_mensaje == "n" or escribir_mensaje == "":
        mensaje = input("hasta luego bro")
        continuar = False
    elif escribir_mensaje == "S" or escribir_mensaje == "s" or escribir_mensaje == "":
        mensaje = input("vamos a pulicar un mensaje.¿que piensas hoy?")
        print()
        print("______________________________________________________")
        print(nombre,"dice",mensaje)
        print("_______________________________________________________")



















