def es_contrasena_segura (contrasena):
 tiene_mayuscula = any(c. isupper() for c in contrasena)
 tiene_numero = any(c.isdigit() for c in contrasena)
 longitud_valida = len (contrasena) > 8
 return tiene_mayuscula and tiene_numero and longitud_valida

#Entrada del usuario
contrasena = input ("Introduce tu contraseña: ")

#Resultado
if es_contrasena_segura (contrasena):
 print ("La contraseña es segura.")
else:
 print ("La contraseña no es segura.")
