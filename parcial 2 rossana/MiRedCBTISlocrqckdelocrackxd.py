print("bienvenido a...")
print()

nombre= input("para empezar dime como te llamas: ")
print()
print("hola", nombre ,"bienvenido a mi red")
print()
agno= int(input("para empezar tu perfil, dime en que año naciste?  "))
edad= 2025-agno-1
print()

estatura= float(input("cuentame ams de ti, para agregarlo a tu perfil. ¿cuantos mides? Dimelo en metros: "))
estatura_m= int(estatura)
estatura_cm= int((estatura - estatura_m)+100 )
print()

telefono= input("ahora dime cual es tu numero de telefono: ")
print()

estado= input("de que estado eres? ")
print()

vivir= input("en donde vives? ")
print()

nacimeinto= input("en donde naciste? ")
print()

sexo= input("cual es tu sexo? ")
print()

direccion= input("cual es tu direccion? ")
num_amigos= int(input("muy bien. finalmente, cuentame cuantos amigos tienes? "))
print()
print("Muy bien", nombre,",Entonces podemos crear tu perfil con estos datos")
print("---------------------------------------------------------------------------")
print("gracias por la informacion. esperamos que disfrutes con la red")
print()
print("estos son tus datos que ingresaste: ")
print("nombre: ",nombre)
print("Año: ", agno)
print("estatura: ", estatura_cm)
print("telefono: ",telefono)
print("estado: ", estado)
print("Lugar en donde vives: ",vivir)
print("naciemiento:",nacimeinto)
print("sexo:", sexo)
print("direccion:",direccion)

continuar= True
while continuar:
    escribir_mensaje=str(input("¿Deseas escribir un mensaje? (S/N) O quieres editar tu nombre escribe, editar "))
    if escribir_mensaje=="S" or escribir_mensaje=="s" or escribir_mensaje=="":
        mensaje = input("Ahora vamos a publicar tu primer mensaje, ¿que piensas hoy?")
        print()
        print("-----------------------------------------------------------------------------")
        print(nombre, "dice : ", mensaje)
        print("-------------------------------------------------------------------------------")
    elif escribir_mensaje == "N" or escribir_mensaje == "n" or escribir_mensaje == "":
        continuar=False
    elif escribir_mensaje== "editar":
        nuevo_nm=input("cual es el nuevo nombre? ")
        print(f"tu nuevo nombre es:",{nombre.replace(nombre,nuevo_nm)})
    else:
        continuar=False

print("Gracias por usar mi red guapo/a")