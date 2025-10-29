import tkinter as tk

def saludar():
    nombre = entrada.get()
    etiqueta_resultado.config(text=f"Hola, {nombre}.")

root = tk.Tk()
root.title("Ejercicio 3 - Entry")
root.geometry("300x200")

etiqueta = tk.Label(root, text="Escribe tu nombre:")
etiqueta.pack(pady=5)

entrada = tk.Entry(root)
entrada.pack(pady=5)

boton = tk.Button(root, text="Saludar", command=saludar)
boton.pack(pady=5)

etiqueta_resultado = tk.Label(root, text="")
etiqueta_resultado.pack(pady=10)

root.mainloop()
