oración = input("POR FAVOR, INGRESE UNA ORACIÓN: ")
palabra_reemplazada = input("INGRESE LA PALABRA QUE DESEE REEMPLAZAR: ")
palabra_de_reemplazo = input("INGRESE LA PALABRA CON LA QUE REEMPLAZARÁ AL ANTERIOR: ")
oración_editada = oración.replace(palabra_reemplazada, palabra_de_reemplazo)
print ("A CONTINUACIÓN LE ESTARÉ MOSTRANDO SU ORACIÓN EDITADA: ")
print (oración_editada)