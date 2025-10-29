import tkinter as tk
from tkinter import messagebox

def añadir_usuario():
    nombre = entry_nombre.get()
    edad = scale_edad.get()
    genero = var_genero.get()
    if nombre:
        lista.insert(tk.END, f"{nombre} - {edad} años - {genero}")
        entry_nombre.delete(0, tk.END)

def eliminar_usuario():
    seleccion = lista.curselection()
    if seleccion:
        lista.delete(seleccion)

def guardar():
    messagebox.showinfo("Guardar", "Lista guardada (simulado)")

def cargar():
    messagebox.showinfo("Cargar", "Lista cargada (simulado)")

def salir():
    root.quit()

root = tk.Tk()
root.title("Ejercicio 12 - Registro de Usuarios")
root.geometry("800x600")

tk.Label(root, text="Nombre:").pack()
entry_nombre = tk.Entry(root)
entry_nombre.pack(pady=5)

tk.Label(root, text="Edad:").pack()
scale_edad = tk.Scale(root, from_=0, to=100, orient="horizontal")
scale_edad.pack(pady=5)

tk.Label(root, text="Género:").pack()
var_genero = tk.StringVar(value="Otro")
tk.Radiobutton(root, text="Masculino", variable=var_genero, value="Masculino").pack()
tk.Radiobutton(root, text="Femenino", variable=var_genero, value="Femenino").pack()
tk.Radiobutton(root, text="Otro", variable=var_genero, value="Otro").pack()

frame_lista = tk.Frame(root)
frame_lista.pack(pady=10, fill="both", expand=True)

lista = tk.Listbox(frame_lista)
lista.pack(side="left", fill="both", expand=True)

scroll = tk.Scrollbar(frame_lista, command=lista.yview)
scroll.pack(side="right", fill="y")
lista.config(yscrollcommand=scroll.set)

tk.Button(root, text="Añadir", command=añadir_usuario).pack(pady=5)
tk.Button(root, text="Eliminar", command=eliminar_usuario).pack(pady=5)
tk.Button(root, text="Salir", command=salir).pack(pady=5)

menu_principal = tk.Menu(root)
root.config(menu=menu_principal)

menu_archivo = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Archivo", menu=menu_archivo)
menu_archivo.add_command(label="Guardar Lista", command=guardar)
menu_archivo.add_command(label="Cargar Lista", command=cargar)

root.mainloop()
