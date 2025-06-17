import tkinter as tk
from tkinter import *

ventana = tk.Tk()

ventana.title("Calculadora de inversión")
ventana.geometry("700x800")
ventana.resizable(False, False)
ventana.minsize(200, 100)
ventana.config(bg="pink")

frame1 = tk.Frame(ventana)
frame1.configure(width=600, height=700, bg="pink", bd=2)
frame1.grid(row=1, column=1)

etiqueta2 = tk.Label(frame1, text="Interés Simple")
etiqueta2.configure(fg="Red", bg="Pink", font=("Comic Sans", 14, "bold"))

etiqueta2.place(x=10, y=10)
frame1.place(x=0, y=0)

entrada1 = tk.Entry(ventana)
entrada1.config(fg="blue", bg="white", font=("Arial", 12))
entrada1.place(x=15, y=100)
ventana.mainloop()