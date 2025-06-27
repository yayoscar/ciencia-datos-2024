import tkinter as tk
from tkinter import messagebox

def guardar_entrada():
    try:
        # Obtener valores de los campos de texto (entradas)
        valor1 = float(entrada1.get())
        valor2 = float(entrada2.get())
        # Mostrar los valores en el label de resultados
        resultado_label.config(text=f"Valores guardados: {valor1} y {valor2}")
        return valor1, valor2
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos")

def sumar():
    try:
        valor1, valor2 = guardar_entrada()
        suma = valor1 + valor2
        resultado_label.config(text=f"Resultado de la suma: {suma}")
    except TypeError:
        pass  # Si hay un error, no hacer nada.

#ventana principal
ventana = tk.Tk()
ventana.title("Operaciones con Entradas")

#para hacer etiquetas
label1 = tk.Label(ventana, text="Ingresa el primer número:")
label1.pack()# .pack() situa en el centro los botones, entradas y demás por default

entrada1 = tk.Entry(ventana)
entrada1.pack()

label2 = tk.Label(ventana, text="Ingresa el segundo número:")
label2.pack()

entrada2 = tk.Entry(ventana)
entrada2.pack()

#Botón para la suma
boton_sumar = tk.Button(ventana, text="Sumar", command=sumar)
boton_sumar.pack()


#Etiqueta que muestra los resultados
resultado_label = tk.Label(ventana, text="Resultado de la operación")
resultado_label.pack()

#Ejecuta la ventana
ventana.mainloop()