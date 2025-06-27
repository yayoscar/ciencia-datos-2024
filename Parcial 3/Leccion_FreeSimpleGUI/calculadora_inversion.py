import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi primera ventana.")
ventana.geometry("700x800")
ventana.resizable(False, True)
ventana.minsize(200,100)
ventana.configure(bg="Gray")
ventana.Button()

ventana.attributes("-alpha, 0.9")
ventana.mainloop()

frame1=tk.Frame(ventana)
frame1.configure(width=600, height=700,bg="pink", bd=2)
frame1.grid(rom=1,colum=1)

etiqueta2=tk.Label(frame1,text=("Interes simple."))
etiqueta2.configure(fg="Baby blue", bg="purple", font=("comic sans",14,"blod"))

etiqueta2.place(x=10,y=10)
