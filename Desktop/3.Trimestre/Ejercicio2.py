#conversor
import tkinter as tk
from tkinter import messagebox

def convertir_c_a_f():
    try:
        c = float(entry.get())
        f = (c * 9/5) + 32
        label_result.config(text=f"{f:.2f} °F")
    except:
        messagebox.showerror("Error", "Introduce un número válido")

def convertir_f_a_c():
    try:
        f = float(entry.get())
        c = (f - 32) * 5/9
        label_result.config(text=f"{c:.2f} °C")
    except:
        messagebox.showerror("Error", "Introduce un número válido")

root = tk.Tk()
root.title("Conversor")
root.geometry("300x180")

tk.Label(root, text="Valor:").pack()
entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="C → F", command=convertir_c_a_f).pack(pady=5)
tk.Button(root, text="F → C", command=convertir_f_a_c).pack(pady=5)

label_result = tk.Label(root, text="")
label_result.pack(pady=10)

root.mainloop()
