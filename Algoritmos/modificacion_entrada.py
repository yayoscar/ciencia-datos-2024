import tkinter as tk
from tkinter import messagebox

def guardar_entrada():
    try:
        valor1 = (entrada1.get())
        valor2 = (entrada2.get())
        valor3 = (entrada3.get())
        valor4 = (entrada4.get())
        resultado_label.config(text=f"Valores guardados: {valor1}, {valor2}, {valor3}, {valor4}")
        return valor1,valor2,valor3,valor4
    except ValueError:
        messagebox.showerror("Error","Por favor ingrese valores válidos.")

def mostrar():
    try:
        valor1, valor2, valor3, valor4 = guardar_entrada()
        resultado_label.config(text=f"Datos: {valor1,valor2,valor3,valor4}")
    except TypeError:
        pass

ventana = tk.Tk()
ventana.title("Datos del usuario.")
ventana.config(bg="lightblue")

label1 = tk.Label(ventana,text="Ingresa tu nombre: ")
label1.pack()

entrada1 = tk.Entry(ventana)
entrada1.pack()

label2 = tk.Label(ventana,text="Ingresa tu edad: ")
label2.pack()

entrada2 = tk.Entry(ventana)
entrada2.pack()

label3 = tk.Label(ventana,text="Ingresa tu sexo: ")
label3.pack()

entrada3 = tk.Entry(ventana)
entrada3.pack()

label4 = tk.Label(ventana,text="Ingresa tu carrera: ")
label4.pack()

entrada4 = tk.Entry(ventana)
entrada4.pack()

boton_mostrar = tk.Button(ventana,text="Mostrar", command=mostrar)
boton_mostrar.configure(bg="pink",fg="blue",font=("Comic Sans",11))
boton_mostrar.pack()

resultado_label = tk.Label(ventana,text="")
resultado_label.pack()

ventana.mainloop()

