#lista de tareas
import tkinter as tk

def agregar():
    tarea = entry.get()
    if tarea != "":
        listbox.insert(tk.END, tarea)
        entry.delete(0, tk.END)

def eliminar():
    seleccion = listbox.curselection()
    if seleccion:
        listbox.delete(seleccion[0])

root = tk.Tk()
root.title("Lista de Tareas")
root.geometry("300x300")

entry = tk.Entry(root)
entry.pack(pady=5)

tk.Button(root, text="Agregar", command=agregar).pack()
tk.Button(root, text="Eliminar", command=eliminar).pack(pady=5)

listbox = tk.Listbox(root)
listbox.pack(expand=True, fill="both", pady=10)

root.mainloop()
