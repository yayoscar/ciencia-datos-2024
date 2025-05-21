print("Bienvendio a")
print("""

LOGO

""")
nombre= input("Para comenzar cual es tu nombre? ")
print()
print("Hola ",nombre, " Bienvenido a esta red social ")
print()
apellidos =input("Ingrese su apellidos: ")
print()
edad= input("Cual es su edad? ")
print("Oh tienes: ",edad)
print()
n1= int(input(" para empezar a crear tu perfil, porfavor  ingrese en que año naciste: "))
print("Oh eres de ",n1, " que genial ")
print()
estatura=  float(input("Para continuar ingrese su estatura o un aproximado: "))
estatura3= (estatura*100)
print("Mides", estatura, "Que interesante ")
print("Y en centimetro serian", estatura3)
n8= input("Cual es tu numero telefonico: ")
n7 = input("Cual es tu direccion: ")
n9= input("Cuan el tu sexo? ")
num_amigos= int(input("Ahora cuantos amigos tienes? "))
print()
print("Su perfil ah quedado asi: ")
print()
print("Su nombre es: ",nombre)
print("Su apellidos son, ", apellidos)
print("Su edad es: ",edad)
print("Tu numero celular es: ",n8)
print("Tu sexo es: ", n9)
print("TU direccion es: ",n7)
print("Su estatura es: ",estatura, " y en centimetros seria: " ,estatura3)
print("______________________________________________________________")
print("Gracias por la informacion, eres Bienvenido a la red")

continuar = True
while continuar :
    n1= str(input("¿Deseas escribir un mensaje? "))
    if n1 == "S" or n1 == "s" or n1 == "":
        mensaje = input("Vamos a publicar este mensaje.¿Que piensas hoy? ")
        print()
        print("_____________________________________________________________")
        print(nombre, "Dice: ", mensaje)
        print("___________________________________________________________")
    elif n1 == "n" or n1 == "N" or n1 == "":
        break
else:
    continuar = False
    print("Hasta la proxima, byeee")
