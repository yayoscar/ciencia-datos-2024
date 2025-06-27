import tkinter as tk

def presionar(boton):
    actual = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(0, actual + str(boton))

def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
    except:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Error")

def limpiar():
    entrada.delete(0, tk.END)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Calculadora Básica")
ventana.geometry("300x400")

# Caja de texto
entrada = tk.Entry(ventana, font=("Arial", 18), borderwidth=5, relief="solid", justify="right")
entrada.pack(padx=10, pady=20, fill="x")

# Botones de la calculadora
botones = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

for fila in botones:
    marco_fila = tk.Frame(ventana)
    marco_fila.pack(expand=True, fill="both")
    for texto in fila:
        if texto == '=':
            b = tk.Button(marco_fila, text=texto, font=("Arial", 16), bg="lightgreen",
                          command=calcular)
        else:
            b = tk.Button(marco_fila, text=texto, font=("Arial", 16),
                          command=lambda x=texto: presionar(x))
        b.pack(side="left", expand=True, fill="both")

# Botón de limpiar
boton_limpiar = tk.Button(ventana, text="Limpiar", font=("Arial", 14), bg="lightcoral",
                          command=limpiar)
boton_limpiar.pack(fill="both", padx=10, pady=10)

ventana.mainloop()
