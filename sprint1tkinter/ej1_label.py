import tkinter as tk

def cambiar_texto():
    etiqueta3.config(text="Texto cambiado!")

root = tk.Tk()
root.title("Ejercicio 1 - Label")
root.geometry("300x200")

etiqueta1 = tk.Label(root, text="Bienvenido a Tkinter")
etiqueta1.pack(pady=5)

etiqueta2 = tk.Label(root, text="Mateo López García")
etiqueta2.pack(pady=5)

etiqueta3 = tk.Label(root, text="Etiqueta inicial")
etiqueta3.pack(pady=5)

boton = tk.Button(root, text="Cambiar texto", command=cambiar_texto)
boton.pack(pady=10)

root.mainloop()
