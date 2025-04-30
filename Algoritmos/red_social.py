from Algoritmos.IMC import estatura

print("bienvenido a...")
print("""""")

#primera interaccion. solicitamos al usuario que ingrese su nombre,
#y lo guardamos en una variable de tipo str
nombre = input("para empezar, dime como te llamas. ")
print()
print("hola ", nombre, ", bienvenido a Mi red")

#segunda interaccion. solicitamos el ingreso del año, y utilizamos este
#dato para estimar la edad de la persona. ¿por que decimos que sol estamos "estimando" su edad?
#¿que ocurre si eliminamos la conversacion a tipo de dato ´int´de la siguiente linea?
agno = int(input("para prepara tu perfil, dime en que año naciste. "))
edad = 2025-agno-1

#tercera interaccion. solicitamos la estatura, medida en metros.
#utilizamos la conversacion a ´int´, y una expresion para convertir esto
#a una medida en metros y centimetros
estatura = float(input("cuentame mas de ti, para agregarlo a tu perfil. ¿cuanto mides? damelo en metros."))
estatura_m = int(estatura)
estatura_cm =  int( (estatura - estatura_m)*100)

#cuarta interaccion. consultamos cuantos amigos tiene el usuario.
num_amigos = int(input("muy bien. finalmente, cuentame cuantos amigos tienes. "))

#con los datos recolectados escribamos en pantalla un textto que resuma los datos que hemos obtenido
print()
print("nombre: ", nombre)
print("------")
print("gracias por la informacion")

print("numero de telefono: 9838094032",)
print("-----------")

print("muy bien. podemos seguir creando este perfil")

print("direccion: AV. lazaro cardenas 86 y 88", )
print("---------")

print("excelente, muy buena infromacion, sigamos creando este perfil.")

print("sexo: mujer", )
print("mujer/hombre: ")

print("gracias, por ultimo esta informacion. ")

print("pais: mexico", )
print("----------")

print("muy bien, gracias por toda la informacion, sigamos creando este perfil con mucho exito. ")
