import tkinter as tk

def agregar_tarea():
    tarea = entrada.get()
    if tarea != "":
        lista.insert(tk.END, tarea)
        entrada.delete(0,tk.END)

def eliminar_tarea():
    seleccionado = lista.curselection()
    if  seleccionado:
        lista.delete(seleccionado)

ventana = tk.Tk()
ventana.title("Lista de tareas")
ventana.geometry("300x300")

entrada = tk.Entry(ventana, width=25)
entrada.pack(pady=5)

tk.Button(ventana,text="Agregar", command=agregar_tarea).pack()
tk.Button(ventana, text="Eliminar", command=eliminar_tarea).pack()

lista = tk.Listbox(ventana)
lista.pack(pady=10, fill=tk.BOTH, expand=True)

ventana.mainloop()
