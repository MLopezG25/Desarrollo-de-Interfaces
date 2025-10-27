import tkinter as tk

def cambiar_color():
    root.config(bg=var.get())

root = tk.Tk()
root.title("Ejercicio 5 - Radiobutton")
root.geometry("300x200")

var = tk.StringVar(value="white")

radio1 = tk.Radiobutton(root, text="Rojo", variable=var, value="red", command=cambiar_color)
radio1.pack()
radio2 = tk.Radiobutton(root, text="Verde", variable=var, value="green", command=cambiar_color)
radio2.pack()
radio3 = tk.Radiobutton(root, text="Azul", variable=var, value="blue", command=cambiar_color)
radio3.pack()

root.mainloop()
