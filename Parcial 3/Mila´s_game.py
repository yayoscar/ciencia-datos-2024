import tkinter as tk
import random

# Variables de puntaje
puntos_jugador = 0
puntos_pc = 0

def jugar(eleccion_usuario):
    global puntos_jugador, puntos_pc
    opciones = ['Piedra', 'Papel', 'Tijeras']
    eleccion_pc = random.choice(opciones)

    if eleccion_usuario == eleccion_pc:
        resultado = "Empate 🤝"
    elif (eleccion_usuario == 'Piedra' and eleccion_pc == 'Tijeras') or \
         (eleccion_usuario == 'Papel' and eleccion_pc == 'Piedra') or \
         (eleccion_usuario == 'Tijeras' and eleccion_pc == 'Papel'):
        resultado = "¡Ganaste! 🎉"
        puntos_jugador += 1
    else:
        resultado = "Perdiste 😢"
        puntos_pc += 1

    etiqueta_resultado.config(
        text=f"Elegiste: {eleccion_usuario}\n"
             f"Computadora: {eleccion_pc}\n"
             f"Resultado: {resultado}"
    )
    actualizar_puntaje()

def actualizar_puntaje():
    etiqueta_puntaje.config(
        text=f"Jugador: {puntos_jugador}  |  Computadora: {puntos_pc}"
    )

# Crear ventana
ventana = tk.Tk()
ventana.title("Piedra, Papel o Tijeras")
ventana.geometry("450x350")
ventana.config(bg="#fde2e2")  # color pastel rosado

# Título
titulo = tk.Label(
    ventana, text="Piedra, Papel o Tijeras",
    font=("Arial", 20, "bold"), bg="#fde2e2", fg="#5c5470"
)
titulo.pack(pady=10)

# Frame de botones
boton_frame = tk.Frame(ventana, bg="#fde2e2")
boton_frame.pack(pady=10)

tk.Button(boton_frame, text="🪨 Piedra", font=("Arial", 12),
          bg="#ffdfd3", fg="#6d597a", width=10,
          command=lambda: jugar('Piedra')).grid(row=0, column=0, padx=5)

tk.Button(boton_frame, text="📄 Papel", font=("Arial", 12),
          bg="#d0f4de", fg="#386641", width=10,
          command=lambda: jugar('Papel')).grid(row=0, column=1, padx=5)

tk.Button(boton_frame, text="✂️ Tijeras", font=("Arial", 12),
          bg="#caffbf", fg="#2a9d8f", width=10,
          command=lambda: jugar('Tijeras')).grid(row=0, column=2, padx=5)

# Resultado
etiqueta_resultado = tk.Label(
    ventana, text="", font=("Arial", 14),
    bg="#fde2e2", fg="#4a4e69"
)
etiqueta_resultado.pack(pady=15)

# Puntaje
etiqueta_puntaje = tk.Label(
    ventana, text="Jugador: 0  |  Computadora: 0",
    font=("Arial", 14, "bold"), bg="#fde2e2", fg="#22223b"
)
etiqueta_puntaje.pack()

# Ejecutar la ventana
ventana.mainloop()
