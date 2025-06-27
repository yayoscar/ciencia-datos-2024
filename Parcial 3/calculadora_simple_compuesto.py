import tkinter as tk
from tkinter import messagebox

# Función para calcular interés simple
def calcular_simple():
    try:
        c = float(entrada_capital.get())
        r = float(entrada_tasa.get())
        t = float(entrada_tiempo.get())
        interes = c * (r / 100) * t
        total = c + interes
        resultado.config(text=f"Interés simple: ${interes:.2f}\nMonto total: ${total:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa valores numéricos válidos.")

# Función para calcular interés compuesto
def calcular_compuesto():
    try:
        c = float(entrada_capital.get())
        r = float(entrada_tasa.get())
        t = float(entrada_tiempo.get())
        total = c * ((1 + (r / 100)) ** t)
        interes = total - c
        resultado.config(text=f"Interés compuesto: ${interes:.2f}\nMonto total: ${total:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa valores numéricos válidos.")

# Ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Interés")
ventana.geometry("300x350")

# Etiquetas y entradas
tk.Label(ventana, text="Capital:", font=("Arial", 12)).pack(pady=5)
entrada_capital = tk.Entry(ventana, font=("Arial", 12))
entrada_capital.pack()

tk.Label(ventana, text="Tasa de interés (%):", font=("Arial", 12)).pack(pady=5)
entrada_tasa = tk.Entry(ventana, font=("Arial", 12))
entrada_tasa.pack()

tk.Label(ventana, text="Tiempo (años):", font=("Arial", 12)).pack(pady=5)
entrada_tiempo = tk.Entry(ventana, font=("Arial", 12))
entrada_tiempo.pack()

# Botones
tk.Button(ventana, text="Calcular Interés Simple", bg="lightgreen", font=("Arial", 12), command=calcular_simple).pack(pady=10)
tk.Button(ventana, text="Calcular Interés Compuesto", bg="lightblue", font=("Arial", 12), command=calcular_compuesto).pack(pady=5)

# Resultado
resultado = tk.Label(ventana, text="", font=("Arial", 12), fg="blue", justify="center")
resultado.pack(pady=20)

ventana.mainloop()
