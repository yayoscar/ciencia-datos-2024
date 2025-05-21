import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task():
    title = entry_title.get().strip()
    due_date = entry_date.get().strip()

    if not title or not due_date:
        messagebox.showwarning("Campos vacíos", "Por favor, completa todos los campos.")
        return

    try:
        due = datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        messagebox.showerror("Formato de fecha inválido", "Usa el formato YYYY-MM-DD.")
        return

    tasks.append({"title": title, "due": due_date})
    save_tasks(tasks)
    entry_title.delete(0, tk.END)
    entry_date.delete(0, tk.END)
    update_task_list()

def update_task_list():
    listbox_tasks.delete(0, tk.END)
    tasks_sorted = sorted(tasks, key=lambda x: x["due"])
    for task in tasks_sorted:
        due_date = datetime.strptime(task["due"], "%Y-%m-%d")
        days_left = (due_date - datetime.now()).days
        if days_left < 0:
            display = f"❌ {task['title']} (Venció el {task['due']})"
        elif days_left ==  0:
            display = f"⚠️ {task['title']} (HOY)"
        elif days_left <= 1:
            display = f"⚠️ {task['title']} (En {days_left} días)"
        else:
            display = f"{task['title']} (Vence: {task['due']})"
        listbox_tasks.insert(tk.END, display)

def delete_selected_task():
    selected = listbox_tasks.curselection()
    if not selected:
        return
    index = selected[0]
    tasks_sorted = sorted(tasks, key=lambda x: x["due"])
    del tasks[tasks.index(tasks_sorted[index])]
    save_tasks(tasks)
    update_task_list()

# Interfaz gráfica
root = tk.Tk()
root.title("Organizador de Tareas para Estudiantes")

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Tarea:").grid(row=0, column=0)
entry_title = tk.Entry(frame, width=30)
entry_title.grid(row=0, column=1)

tk.Label(frame, text="Fecha (YYYY-MM-DD):").grid(row=1, column=0)
entry_date = tk.Entry(frame)
entry_date.grid(row=1, column=1)

tk.Button(frame, text="Agregar tarea", command=add_task).grid(row=2, columnspan=2, pady=5)

listbox_tasks = tk.Listbox(root, width=60, height=10)
listbox_tasks.pack()

tk.Button(root, text="Eliminar tarea seleccionada", command=delete_selected_task).pack(pady=5)

# Cargar y mostrar tareas
tasks = load_tasks()
update_task_list()

root.mainloop()
