import tkinter as tk
from tkinter import messagebox  # Librería para los mensajes

# Lista para guardar los contactos
agenda = []

# Función para agregar contacto
def agregar_contacto():
    nombre = entrada_nombre.get()
    telefono = entrada_telefono.get()
    correo = entrada_correo.get()

    if nombre and telefono and correo:
        contacto = f"{nombre} | {telefono} | {correo}"
        agenda.append(contacto)  # agrega un elemento al final de una lista
        actualizar_lista()

        # Dejar vacías las entradas
        entrada_nombre.delete(0, tk.END)
        entrada_telefono.delete(0, tk.END)
        entrada_correo.delete(0, tk.END)
    else:
        # Mensaje de error al dejar vacío algún campo
        messagebox.showerror("Error", "Por favor completa todos los campos.")

# Función para eliminar contacto
def eliminar_contacto():
    seleccion = lista.curselection()
    if seleccion:
        indice = seleccion[0]
        agenda.pop(indice)  # elimina el elemento de la lista
        actualizar_lista()
    else:
        # Mostrar mensaje de error si no seleccionaste ningún registro
        messagebox.showwarning("Atención", "Selecciona un contacto para eliminar.")

# Función para actualizar la lista visual
def actualizar_lista():
    lista.delete(0, tk.END)
    for contacto in agenda:
        lista.insert(tk.END, contacto)

# Interfaz
ventana = tk.Tk()
ventana.title("Agenda de Contactos")
ventana.geometry("400x400")

# Estilo general para etiquetas
estilo_label = {"font": ("Arial", 12), "padx": 5, "pady": 5}
estilo_entry = {"width": 40}

# Label y entrada para nombre
tk.Label(ventana, text="Nombre:", **estilo_label).pack()
entrada_nombre = tk.Entry(ventana, **estilo_entry)
entrada_nombre.pack()

# Label y entrada para teléfono
tk.Label(ventana, text="Teléfono:", **estilo_label).pack()
entrada_telefono = tk.Entry(ventana, **estilo_entry)
entrada_telefono.pack()

# Label y entrada para correo
tk.Label(ventana, text="Correo:", **estilo_label).pack()
entrada_correo = tk.Entry(ventana, **estilo_entry)
entrada_correo.pack()

# Botones
tk.Button(ventana, text="Agregar Contacto", command=agregar_contacto).pack(pady=10)
tk.Button(ventana, text="Eliminar Contacto Seleccionado", command=eliminar_contacto).pack()

# Lista
lista = tk.Listbox(ventana, width=50)
lista.pack(pady=10, fill=tk.BOTH, expand=True)

ventana.mainloop()