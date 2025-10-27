import tkinter as tk

def mostrar_fruta():
    seleccion = listbox.curselection()
    if seleccion:
        fruta = listbox.get(seleccion[0])
        etiqueta.config(text="Fruta seleccionada: " + fruta)

root = tk.Tk()
root.title("Ejercicio 6 - Listbox")
root.geometry("300x250")

listbox = tk.Listbox(root)
listbox.pack(pady=10)

for fruta in ["Manzana", "Banana", "Naranja"]:
    listbox.insert(tk.END, fruta)

boton = tk.Button(root, text="Mostrar selección", command=mostrar_fruta)
boton.pack(pady=5)

etiqueta = tk.Label(root, text="Fruta seleccionada: Ninguna")
etiqueta.pack(pady=10)

root.mainloop()
