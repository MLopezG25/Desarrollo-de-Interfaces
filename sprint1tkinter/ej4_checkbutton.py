import tkinter as tk

def actualizar():
    seleccionadas = []
    if var1.get():
        seleccionadas.append("Leer")
    if var2.get():
        seleccionadas.append("Deporte")
    if var3.get():
        seleccionadas.append("Música")
    etiqueta.config(text="Aficiones: " + ", ".join(seleccionadas))

root = tk.Tk()
root.title("Ejercicio 4 - Checkbutton")
root.geometry("300x200")

var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()

check1 = tk.Checkbutton(root, text="Leer", variable=var1, command=actualizar)
check1.pack()
check2 = tk.Checkbutton(root, text="Deporte", variable=var2, command=actualizar)
check2.pack()
check3 = tk.Checkbutton(root, text="Música", variable=var3, command=actualizar)
check3.pack()

etiqueta = tk.Label(root, text="Aficiones: ")
etiqueta.pack(pady=10)

root.mainloop()
