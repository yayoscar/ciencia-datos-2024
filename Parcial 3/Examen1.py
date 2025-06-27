import tkinter as tk
from tkinter import messagebox # Importar la librería de mensajes

# Lista para almacenar los productos
productos = []

# Función para guardar datos
def registrar_producto ():
    nombre =  entrada_nombre.get ()
    cantidad = entrada_cantidad.get ()
    costo = entrada_costo.get ()

    # Validación de campos
    if not nombre or not cantidad.isdigit () or not costo.replace ('.','',1).isdigit ():
        messagebox.showerror("Error", "Completa todos los campos correctamente.\nCantidad y costo deben ser númericos.")
        return

     cantidad = int(cantidad)
     costo = float(costo)

     producto = f"{nombre} - Cantidad: {cantidad} - Costo: ${costo:.2f}"
     productos.append(producto)

     # Mostrar en el listbox
     listbox_productos.insert(tk.END, producto)

     # Limpiar entradas
     entrada_nombre.delete(0, tk.END)
     entrada_costo.delete(0, tk.END)
     entrada_cantidad.delete(0,tk.END)

     # Mensaje de confirmación
     (messagebox_showinfo("Éxito", "Producto registrado correctamente."))

# Crear ventana
ventana = tk.Tk ()
ventana.title("Registro de Inventario")
ventana.geometry("450X450")

# Etiquetas y entredas
tk.Label (ventana, text="Nombre del producto:").pack()
entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack(pady=5)

tk.Label(ventana, text="Cantidad:").pack()
entrada_cantidad = tk.Entry(ventana)
entrada_cantidad.pack(pady=5)

tk.Label(ventana, text="Costo:").pack()
entrada_costo = tk.Entry(ventana)
entrada_costo.pack(pady=5)

# Botón para registrar
tk.Button(ventana, text="Registrar Producto", command=registrar_producto).pack(pady=10)

# Listbox para mostrar producto registrados
tk.Label(ventana, text= "Productos registrados:").pack(pady=5)
listbox_productos = tk.Listbox(ventana, width=50)
listbox_productos.pack(pady=10)

# Ejecutar la aplicación
ventana.mainloop()