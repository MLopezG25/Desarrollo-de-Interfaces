import tkinter as tk

def mostrar_mensaje():
    etiqueta.config(text="¡Has pulsado el botón!")

root = tk.Tk()
root.title("Ejercicio 2 - Button")
root.geometry("300x150")

etiqueta = tk.Label(root, text="")
etiqueta.pack(pady=10)

boton1 = tk.Button(root, text="Mostrar mensaje", command=mostrar_mensaje)
boton1.pack(pady=5)

boton2 = tk.Button(root, text="Salir", command=root.quit)
boton2.pack(pady=5)

root.mainloop()
