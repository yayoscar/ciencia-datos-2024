import tkinter as tk
from tkinter import simpledialog, messagebox

def ingresar_dato(tipo):
    dato = simpledialog.askstring("Entrada de dato", f"Ingrese su {tipo}:")
    if dato:
        datos[tipo] = dato
        actualizar_display()

def actualizar_display():
    texto = ""
    for clave, valor in datos.items():
        texto += f"{clave}: {valor}\n"
    pantalla.config(state='normal')
    pantalla.delete("1.0", tk.END)
    pantalla.insert(tk.END, texto)
    pantalla.config(state='disabled')

def mostrar_datos():
    if all(campo in datos for campo in campos):
        messagebox.showinfo("Datos Completos", "\n".join(f"{k}: {v}" for k, v in datos.items()))
    else:
        messagebox.showwarning("Faltan datos", "Por favor, ingresa todos los datos.")

# Datos personales a pedir
campos = ["Nombre", "Edad", "Sexo", "Dirección", "Teléfono"]
datos = {}

# Ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Datos Personales")
ventana.geometry("300x400")

# Pantalla tipo display
pantalla = tk.Text(ventana, height=10, width=30, state='disabled', bg='lightyellow')
pantalla.pack(pady=10)

# Crear botones tipo calculadora para cada dato
for campo in campos:
    tk.Button(ventana, text=f"Ingresar {campo}", width=25, command=lambda c=campo: ingresar_dato(c)).pack(pady=3)

# Botón para mostrar los datos
tk.Button(ventana, text="Mostrar Datos", bg="lightblue", width=25, command=mostrar_datos).pack(pady=10)

ventana.mainloop()
