import tkinter as tk
from tkinter import messagebox

from pygame.transform import rotozoom


def guardar_datos():
    try:
        # Obtener valores de los campos de texto(entradas)
        valor1 = (entrada1.get())
        valor2 = (entrada2.get())
        valor3 = (entrada3.get())
        valor4 = (entrada4.get())
        # Mostrar los valores en el label de resultados.
        resultado_label.config(text = f"Valores guardados:{valor1}, {valor2}, {valor3}, {valor4}")
        return valor1, valor2, valor3, valor4
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese valores válidos.")

def mostrar():
    try:
        valor1, valor2, valor3, valor4 = guardar_datos()
        resultado_label.config(text=f"Datos: {valor1}, \n{valor2}, \n{valor3}, \n{valor4}")
    except TypeError:
        pass # Si hay un error, no hacer nada.

ventana = tk.Tk()
ventana.title("Datos con estradas")

# Para hacer etiquetas.
label1 = tk.Label(ventana, text="Nombre:")
label1.config(font=("Bell MT", 15))
label1.pack() # .pack() situa en el centro los botones, entradas y demás por default.

entrada1 = tk.Entry(ventana)
entrada1.pack()

label2 = tk.Label(ventana, text="Edad:")
label2.config(font=("Bell MT", 15))
label2.pack()

entrada2 = tk.Entry(ventana)
entrada2.pack()

# Para hacer etiquetas.
label3 = tk.Label(ventana, text="Sexo:")
label3.config(font=("Bell MT", 15))
label3.pack() # .pack() situa en el centro los botones, entradas y demás por default.

entrada3 = tk.Entry(ventana)
entrada3.pack()

label4 = tk.Label(ventana, text="Carrera:")
label4.config(font=("Bell MT", 15))
label4.pack()

entrada4 = tk.Entry(ventana)
entrada4.pack()

boton_mostrar = tk.Button(ventana, text="Mostrar datos", command=mostrar)
boton_mostrar.config(bg="purple", font=("Bell MT", 15))
boton_mostrar.pack()


resultado_label = tk.Label(ventana, text="Datos")
resultado_label.config(font=("Bell MT", 15))
resultado_label.pack()

# Ejecuta la ventana.
ventana.mainloop()
