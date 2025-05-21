password = input("password: ")

if len(password) >=8:
    print("largo correcto")
else:
    print("largo incorrecto")

    digito = False
    for letra in password:
        if letra.isdigit():
            digito = True

    digito