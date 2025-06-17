import tkinter as tk
from tkinter import messagebox, ttk

from pygame.transform import rotozoom


def guardar_entrada():
    try:
        # Obtener valores de los campos de texto(entradas)
        valor1 = float(entrada1.get())
        valor2 = float(entrada2.get())
        # Mostrar los valores en el label de resultados.
        resultado_label.config(text = f"Valores guardados:{valor1}, {valor2}")
        return valor1, valor2
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos.")

def sumar():
    try:
        valor1, valor2 = guardar_entrada()
        suma = valor1 + valor2
        resultado_label.config(text=f"Resultado de la suma {suma}")
    except TypeError:
        pass # Si hay un error, no hacer nada.

def restar():
    try:
        valor1, valor2 = guardar_entrada()
        resta = valor1 - valor2
        resultado_label.config(text=f"Resultado de la resta {resta}")
    except TypeError:
        pass # Si hay un error, no hacer nada.

def multiplicar():
    try:
        valor1, valor2 = guardar_entrada()
        multiplicacion = valor1 * valor2
        resultado_label.config(text=f"Resultado de la multiplicación {multiplicacion}")
    except TypeError:
        pass # Si hay un error, no hacer nada.

def dividir():
    try:
        valor1, valor2 = guardar_entrada()
        division = valor1 / valor2
        resultado_label.config(text=f"Resultado de la división {division}")
    except TypeError:
        pass # Si hay un error, no hacer nada.

# Ventana prinicipal.
ventana = tk.Tk()
ventana.title("Operaciones con Entradas.")

# Para hacer etiquetas.
label1 = tk.Label(ventana, text="Ingresa el primer número:")
label1.config(font=("Bell MT", 15))
label1.pack() # .pack() situa en el centro los botones, entradas y demás por default.

entrada1 = tk.Entry(ventana)
entrada1.pack()

label2 = tk.Label(ventana, text="Ingresa el segundo número:")
label2.config(font=("Bell MT", 15))
label2.pack()

entrada2 = tk.Entry(ventana)
entrada2.pack()

# Boton para la suma.
boton_sumar = tk.Button(ventana, text="Sumar", command=sumar)
boton_sumar.config(bg="purple", font=("Bell MT", 15))
boton_sumar.pack()

boton_restar = tk.Button(ventana, text="Restar", command=restar)
boton_restar.config(bg="purple", font=("Bell MT", 15))
boton_restar.pack()

boton_multiplicar = tk.Button(ventana, text="Multiplicar", command=multiplicar)
boton_multiplicar.config(bg="purple", font=("Bell MT", 15))
boton_multiplicar.pack()

boton_dividir = tk.Button(ventana, text="Dividir", command=dividir)
boton_dividir.config(bg="purple", font=("Bell MT", 15))
boton_dividir.pack()

# Etiqueta que muestra los resultados.
resultado_label = tk.Label(ventana, text="Reultado de la operación")
resultado_label.config(font=("Bell MT", 15))
resultado_label.pack()

# Ejecuta la ventana.
ventana.mainloop()