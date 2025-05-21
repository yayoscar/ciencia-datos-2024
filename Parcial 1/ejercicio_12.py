felix_essential = ["brownies", "deep voice", "smile", "sunshine", "freckles"]  # Convertido a lista
palabra_eliminar = input("¿Qué palabra le gustaría eliminar de la oración? ")

if palabra_eliminar in felix_essential:
    felix_essential.remove(palabra_eliminar)
    print(f"La lista de palabras después de eliminar '{palabra_eliminar}' es: {felix_essential}")
else:
    print(f"La palabra '{palabra_eliminar}' no se encuentra en la lista.")

