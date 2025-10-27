import tkinter as tk

def mostrar():
    etiqueta_resultado.config(text=entrada.get())

def borrar():
    entrada.delete(0, tk.END)
    etiqueta_resultado.config(text="")

root = tk.Tk()
root.title("Ejercicio 8 - Frame")
root.geometry("400x200")

frame_superior = tk.Frame(root, bg="lightgrey")
frame_superior.pack(fill="x", padx=10, pady=10)

tk.Label(frame_superior, text="Etiqueta 1").grid(row=0, column=0, padx=5, pady=5)
tk.Label(frame_superior, text="Etiqueta 2").grid(row=0, column=1, padx=5, pady=5)

entrada = tk.Entry(frame_superior)
entrada.grid(row=1, column=0, columnspan=2, pady=5)

frame_inferior = tk.Frame(root, bg="white")
frame_inferior.pack(fill="x", padx=10, pady=10)

tk.Button(frame_inferior, text="Mostrar", command=mostrar).grid(row=0, column=0, padx=5)
tk.Button(frame_inferior, text="Borrar", command=borrar).grid(row=0, column=1, padx=5)

etiqueta_resultado = tk.Label(frame_inferior, text="")
etiqueta_resultado.grid(row=1, column=0, columnspan=2, pady=10)

root.mainloop()
