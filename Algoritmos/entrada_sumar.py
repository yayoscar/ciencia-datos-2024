import tkinter as tk
from tkinter import messagebox

def guardar_entrada():
    try:
        valor1 = float(entrada1.get())
        valor2 = float(entrada2.get())
        resultado_label.config(text=f"Valores guardados: {valor1} y {valor2}")
        return valor1,valor2
    except ValueError:
        messagebox.showerror("Error","Por favor ingrese valores numéricos válidos.")

def sumar():
    try:
        valor1,valor2 = guardar_entrada()
        suma = valor1 + valor2
        resultado_label.config(text=f"Resultado de la suma: {suma}")
    except TypeError:
        pass

def multiplicar():
    try:
        valor1,valor2 = guardar_entrada()
        multiplicacion = valor1 * valor2
        resultado_label.config(text=f"Resultado de la multiplicacion: {multiplicacion}")
    except TypeError:
        pass

def dividir():
    try:
        valor1,valor2 = guardar_entrada()
        division = valor1/valor2
        resultado_label.config(text=f"Resultado de la divicion: {division}")
    except TypeError:
        pass

def restar():
    try:
        valor1,valor2 = guardar_entrada()
        resta = valor1-valor2
        resultado_label.config(text=f"Resultado de la resta: {resta}")
    except TypeError:
        pass

ventana = tk.Tk()
ventana.title("Operaciones con entradas.")

label1 = tk.Label(ventana,text="Ingresa el primer número:")
label1.pack()

entrada1 = tk.Entry(ventana)
entrada1.pack()

label2 = tk.Label(ventana,text="Ingresa el segundo número: ")
label2.pack()

entrada2 = tk.Entry(ventana)
entrada2.pack()

boton_sumar = tk.Button(ventana,text="Sumar",command=sumar)
boton_sumar.configure(bg="pink",fg="blue",font=("Comic Sans",11))
boton_sumar.pack()

boton_multiplicar = tk.Button(ventana,text="Multiplicar",command=multiplicar)
boton_multiplicar.configure(bg="pink",fg="blue",font=("Comic Sans",11))
boton_multiplicar.pack()

boton_dividir = tk.Button(ventana,text="Dividir",command=dividir)
boton_dividir.configure(bg="pink",fg="blue",font=("Comic Sans",11))
boton_dividir.pack()

boton_restar = tk.Button(ventana,text="Restar",command=restar)
boton_restar.configure(bg="pink",fg="Blue",font=("Comic Sans",11))
boton_restar.pack()

resultado_label = tk.Label(ventana,text="Resultado de la operación: ")
resultado_label.pack()

ventana.mainloop()

