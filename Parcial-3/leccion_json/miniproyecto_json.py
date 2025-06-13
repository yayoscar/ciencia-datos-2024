import json
import os

from numpy.version import release


def cargar_agenda():
    if os.path.exists("agenda.json"):
        with open("agenda.json", "r") as archivo:
            return json.load(archivo)

def guardar_agenda(agenda):
    with open("agenda.json","w") as archivo:
        json.dump(agenda,archivo,indent=4)
        #indent para que sea leible para humanos

def agregar_contacto(agenda):
    nombre = input("Nombre: ")
    telefono = input("Telefono: ")
    email = input("Email: ")

    contacto = {
        "nombre": nombre,
        "telefono": telefono,
        "email":email
    }
    agenda.append(contacto)
    print("Contacto agregado:)")

def main():
    agenda = cargar_agenda()
    print("Agenda cargada. Contactos actuales", len(agenda))

    while True:
        opcion = input("¿Deseas agregar un contacto? (S/N): ").lower()
        if opcion == "s":
            agregar_contacto(agenda)
        else:
            break

    guardar_agenda((agenda))
    print("agenda guardada en agenda.json:)")

if __name__ == "__main__":
    main()