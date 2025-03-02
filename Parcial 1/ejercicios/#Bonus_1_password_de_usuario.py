#Bonus 1
#Programa que pide un password al usuario hasta que sea el correcto
password_correcto = "cienciadedatos"
password = ""

while password != password_correcto:
    password = input("password: ")
print ("Acceso correcto")