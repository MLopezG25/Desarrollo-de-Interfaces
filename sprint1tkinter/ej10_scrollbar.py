import tkinter as tk

root = tk.Tk()
root.title("Ejercicio 10 - Scrollbar")
root.geometry("300x300")

# Widget Text
texto = tk.Text(root, wrap="word")
texto.pack(side="left", fill="both", expand=True)

# Scrollbar vertical
scroll = tk.Scrollbar(root, command=texto.yview)
scroll.pack(side="right", fill="y")

texto.config(yscrollcommand=scroll.set)

# Insertar texto largo
for i in range(1, 101):
    texto.insert(tk.END, f"Línea {i}\n")

root.mainloop()
