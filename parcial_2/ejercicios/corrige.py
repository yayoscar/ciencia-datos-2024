''' Corregir:
if edad > 60 or edad < 18 and vive_en_mexico:
'''
edad = int(input("Edad: "))
vive_en_mexico = input("vives en mexico?")
if vive_en_mexico == "si":
    vive_en_mexico = True
else:
    vive_en_mexico = False
if (edad > 60 or edad < 18) and vive_en_mexico == True:
    print("Sí")
else:
    print("No")