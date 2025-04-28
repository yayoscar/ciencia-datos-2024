#CONCATENACIÓN DE CADENAS

saludo = "hola"
destinatario = "Mundo"
saludo_completo = saludo + destinatario
print(saludo_completo)

#AGREGAR SEPARADORES A LA CONCATENACIÓN

saludo = "hola"
separador = ", "
destinatario = "Mundo"
puntuación = "!"
saludo_completo = saludo + separador +destinatario + puntuación
print(saludo_completo)

#EL SIGNO + SOLO FUNCIONA ENTRE CADENAS, SI COMBINAS UNA CADENA Y NÚMERO PYTHON MOSTRARA ERROR:
# print("La suma de 2 más 2 es" + 4) = ERROR
# TIENE QUE SER DE LA SIGUIENTE MANERA=

print("La suma de 2 más 2 es " + str(4)) #CORRECTO
