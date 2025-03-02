print("ingresa la frase que quieras")
frase = input("")

print("ingresa una nueva palabra  ")
new_word = input("")

print("ingresa una frase por la que quieras reemplazar")
old_word = input("")


frase_nueva = frase.replace(old_word, new_word)
print(frase_nueva)
