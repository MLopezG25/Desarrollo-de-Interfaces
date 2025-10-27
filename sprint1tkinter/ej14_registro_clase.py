import tkinter as tk
from tkinter import messagebox

class RegistroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ejercicio 14 - Registro con Clase")
        self.root.geometry("400x400")

        tk.Label(root, text="Nombre:").pack()
        self.entry_nombre = tk.Entry(root)
        self.entry_nombre.pack(pady=5)

        tk.Label(root, text="Edad:").pack()
        self.scale_edad = tk.Scale(root, from_=0, to=100, orient="horizontal")
        self.scale_edad.pack(pady=5)

        tk.Label(root, text="Género:").pack()
        self.var_genero = tk.StringVar(value="Otro")
        tk.Radiobutton(root, text="Masculino", variable=self.var_genero, value="Masculino").pack()
        tk.Radiobutton(root, text="Femenino", variable=self.var_genero, value="Femenino").pack()
        tk.Radiobutton(root, text="Otro", variable=self.var_genero, value="Otro").pack()

        frame_lista = tk.Frame(root)
        frame_lista.pack(pady=10, fill="both", expand=True)

        self.lista = tk.Listbox(frame_lista)
        self.lista.pack(side="left", fill="both", expand=True)

        scroll = tk.Scrollbar(frame_lista, command=self.lista.yview)
        scroll.pack(side="right", fill="y")
        self.lista.config(yscrollcommand=scroll.set)

        tk.Button(root, text="Añadir", command=self.añadir_usuario).pack(pady=5)
        tk.Button(root, text="Eliminar", command=self.eliminar_usuario).pack(pady=5)
        tk.Button(root, text="Salir", command=self.salir).pack(pady=5)

        menu_principal = tk.Menu(root)
        root.config(menu=menu_principal)

        menu_archivo = tk.Menu(menu_principal, tearoff=0)
        menu_principal.add_cascade(label="Archivo", menu=menu_archivo)
        menu_archivo.add_command(label="Guardar Lista", command=self.guardar)
        menu_archivo.add_command(label="Cargar Lista", command=self.cargar)

    def añadir_usuario(self):
        nombre = self.entry_nombre.get()
        edad = self.scale_edad.get()
        genero = self.var_genero.get()
        if nombre:
            self.lista.insert(tk.END, f"{nombre} - {edad} años - {genero}")
            self.entry_nombre.delete(0, tk.END)

    def eliminar_usuario(self):
        seleccion = self.lista.curselection()
        if seleccion:
            self.lista.delete(seleccion)

    def guardar(self):
        messagebox.showinfo("Guardar", "Lista guardada (simulado)")

    def cargar(self):
        messagebox.showinfo("Cargar", "Lista cargada (simulado)")

    def salir(self):
        self.root.quit()

root = tk.Tk()
app = RegistroApp(root)
root.mainloop()
