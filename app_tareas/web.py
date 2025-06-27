import funciones_main
import streamlit as st

def agregar_tarea():
    if 'tarea_nueva' in st.session_state:
        nueva_tarea = f"{st.session_state['tarea_nueva']}\n"
        tareas.append(nueva_tarea)
        funciones_main.guardar_tareas(tareas)
        st.rerun()

tareas = funciones_main.leer_tareas()

st.title("Lista de tareas")
st.subheader("Desarrollado por Oscar Perez")
st.badge("Ciencia de Datos 2025",color="blue")

for index,tarea in enumerate(tareas):
    checkbox=st.checkbox(tarea,key=f"tarea{index}")
    if checkbox:
        tareas.pop(index)
        funciones_main.guardar_tareas(tareas)
        del st.session_state[f"tarea{index}"]
        st.rerun()

st.text_input(label="Agregar Tarea",placeholder="Agregar Tarea",key="tarea_nueva",on_change=agregar_tarea())

