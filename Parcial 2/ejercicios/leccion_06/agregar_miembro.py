def agregar_miembro():
    try:
        with open('miembros.txt', 'a') as archivo:
            nuevo_miembro = input("Agregar nuevo miembro: ")
            archivo.write(nuevo_miembro + "\n")
        print("Miembro agregado con éxito.")
    except Exception as e:
        print(f"Error al agregar miembro: {e}")