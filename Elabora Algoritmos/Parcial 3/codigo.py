import tkinter as tk
from tkinter import messagebox
from openpyxl import Workbook, load_workbook
import os

nombre_archivo = "CBTis72.xlsx"
if os.path.exists(nombre_archivo):

    wb = load_workbook(nombre_archivo)
    ws = wb.active
else:
    wb = Workbook()
    ws = wb.active
    ws.append(["Nombre", "Edad", "Carrera", "Curp", "Semestre", "No. Control", "Sexo", "Dirección", "Teléfono", "Tipo de sangre"])

def guardar_datos():
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    direccion = entry_direccion.get()
    control = entry_control.get()
    carrera = entry_carrera.get()
    sexo = entry_sexo.get()
    sangre = entry_sangre.get()
    semestre = entry_semestre.get()
    curp = entry_curp.get()
    telefono = entry_telefono.get()

    if not nombre or not edad:
        messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")
        return
    try:
        edad = int(edad)
    except ValueError:
        messagebox.showwarning("Advertencia", "edad")
        return

    ws.append([nombre, edad, direccion, control, carrera, sexo, sangre, semestre, curp, telefono])
    wb.save(nombre_archivo)

    messagebox.showinfo("Inofrmación", "Los datos se han guardado con éxito")
    entry_nombre.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    entry_direccion.delete(0, tk.END)
    entry_control.delete(0, tk.END)
    entry_carrera.delete(0, tk.END)
    entry_sexo.delete(0, tk.END)
    entry_sangre.delete(0, tk.END)
    entry_semestre.delete(0, tk.END)
    entry_curp.delete(0, tk.END)
    entry_telefono.delete(0, tk.END)

ventana = tk.Tk()
ventana.title("Registro de alumnos del CBTIS 72")
ventana.configure(bg="Blue")
label_style = {"bg": "blue", "fg": "white"}
entry_style = {"bg": "green", "fg": "black"}

label_nombre = tk.Label(ventana, text="Nombre", **label_style)
label_nombre.grid(row=0, column=0, padx=10, pady=5)
entry_nombre = tk.Entry(ventana, **entry_style)
entry_nombre.grid(row=0, column=1, padx=10, pady=5)

label_edad = tk.Label(ventana, text="Edad", **label_style)
label_edad.grid(row=2, column=0, padx=10, pady=5)
entry_edad = tk.Entry(ventana, **entry_style)
entry_edad.grid(row=2, column=1, padx=10, pady=5)

label_carrera = tk.Label(ventana, text="Carrera", **label_style)
label_carrera.grid(row=4, column=0, padx=10, pady=5)
entry_carrera = tk.Entry(ventana, **entry_style)
entry_carrera.grid(row=4, column=1, padx=10, pady=5)

label_curp = tk.Label(ventana, text="Curp", **label_style)
label_curp.grid(row=6, column=0, padx=10, pady=5)
entry_curp = tk.Entry(ventana, **entry_style)
entry_curp.grid(row=6, column=1, padx=10, pady=5)

label_semestre = tk.Label(ventana, text="Semestre", **label_style)
label_semestre.grid(row=8, column=0, padx=10, pady=5)
entry_semestre = tk.Entry(ventana, **entry_style)
entry_semestre.grid(row=8, column=1, padx=10, pady=5)

label_control = tk.Label(ventana, text="No. Control", **label_style)
label_control.grid(row=8, column=2, padx=10, pady=5)
entry_control = tk.Entry(ventana, **entry_style)
entry_control.grid(row=8, column=4, padx=10, pady=5)

label_sexo = tk.Label(ventana, text="Sexo", **label_style)
label_sexo.grid(row=2, column=2, padx=10, pady=5)
entry_sexo = tk.Entry(ventana, **entry_style)
entry_sexo.grid(row=2, column=4, padx=10, pady=5)

label_telefono = tk.Label(ventana, text="Teléfono", **label_style)
label_telefono.grid(row=16, column=0, padx=10, pady=5)
entry_telefono = tk.Entry(ventana, **entry_style)
entry_telefono.grid(row=16, column=1, padx=10, pady=5)

label_sangre = tk.Label(ventana, text="Tipo de sangre", **label_style)
label_sangre.grid(row=16, column=2, padx=10, pady=5)
entry_sangre = tk.Entry(ventana, **entry_style)
entry_sangre.grid(row=16, column=4, padx=10, pady=5)

label_direccion = tk.Label(ventana, text="Dirección", **label_style)
label_direccion.grid(row=18, column=0, padx=10, pady=5)
entry_direccion = tk.Entry(ventana, **entry_style)
entry_direccion.grid(row=18, column=1, padx=10, pady=5)

boton_guardar = tk.Button(ventana, text="Guardar", command=guardar_datos, bg="blue", fg="black")
boton_guardar.grid(row=20, column=0, columnspan=2 ,padx=10, pady=10)

ventana.mainloop()