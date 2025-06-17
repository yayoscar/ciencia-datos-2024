import tkinter as tk

def calcular_interes_simple(capital, tasa, tiempo):
    return capital * tasa * tiempo

def calcular_interes_compuesto(capital, tasa, tiempo):
    monto = capital
    for _ in range(tiempo):
        monto += monto * tasa
    return monto

def calcular_interes():
    try:
        capital = float(entry_capital.get())
        tasa = float(entry_tasa.get()) / 100
        tiempo = int(entry_tiempo.get())
        tipo = tipo_var.get()

        if tipo == "simple":
            interes = calcular_interes_simple(capital, tasa, tiempo)
            total = capital + interes
            resultado.config(text=f"Interés simple: {interes:.2f}\nMonto total: {total:.2f}", font=("Arial", 12))
        elif tipo == "compuesto":
            total = calcular_interes_compuesto(capital, tasa, tiempo)
            interes = total - capital
            resultado.config(text=f"Interés compuesto: {interes:.2f}\nMonto total: {total:.2f}", font=("Arial", 12))
        else:
            resultado.config(text="Elige un tipo de interés")
    except:
        resultado.config(text="Revisa los datos ingresados")

ventana = tk.Tk()
ventana.title('Mi ventanita')
ventana.geometry('400x300')
ventana.config(bg='purple')

tk.Label(ventana, text="Capital:", bg='purple', fg='white', font=("Arial", 14)).pack()
entry_capital = tk.Entry(ventana)
entry_capital.pack()

tk.Label(ventana, text="Tasa (%):", bg='purple', fg='white', font=("Arial", 14)).pack()
entry_tasa = tk.Entry(ventana)
entry_tasa.pack()

tk.Label(ventana, text="Tiempo (años):", bg='purple', fg='white', font=("Arial", 14)).pack()
entry_tiempo = tk.Entry(ventana)
entry_tiempo.pack()

tipo_var = tk.StringVar()
tk.Radiobutton(ventana, text="Simple", variable=tipo_var, value="simple", bg='purple', fg='white', font=("Arial", 12)).pack()
tk.Radiobutton(ventana, text="Compuesto", variable=tipo_var, value="compuesto", bg='purple', fg='white', font=("Arial", 12)).pack()

tk.Button(ventana, text="Calcular", command=calcular_interes).pack(pady=10)
resultado = tk.Label(ventana, text="", bg='purple', fg='white')
resultado.pack()

ventana.mainloop()