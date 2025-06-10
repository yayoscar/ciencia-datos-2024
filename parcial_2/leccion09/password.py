password = input("Password: ")

if len(password) >=8:
    print("largo correcto")
else:
    print("largo incorrecto")

mayuscula = False
for letra in password:
    if letra.isuper():
        mayusculas = True

if mayusculas:
    print("cumple con mayusculas")
else:
    print("no cumple con mayusculas")
else:
print 


