import tkinter as tk

def dibujar_circulo(event):
    x, y = event.x, event.y
    canvas.create_oval(x-20, y-20, x+20, y+20, fill="blue")

def borrar(event):
    if event.char == "c":
        canvas.delete("all")

root = tk.Tk()
root.title("Ejercicio 13 - Eventos")
root.geometry("400x300")

canvas = tk.Canvas(root, bg="white")
canvas.pack(fill="both", expand=True)

canvas.bind("<Button-1>", dibujar_circulo)
root.bind("<Key>", borrar)

root.mainloop()
