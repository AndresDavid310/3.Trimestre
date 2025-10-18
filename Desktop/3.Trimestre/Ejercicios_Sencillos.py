# calculadora_basica_suma.py
import tkinter as tk  # Importar Tkinter

# ---- Función ----
def sumar():
    try:
        n1 = float(entrada1.get())   # tomar el valor del primer número
        n2 = float(entrada2.get())   # tomar el valor del segundo número
        resultado.set(n1 + n2)       # mostrar el resultado
    except ValueError:
        resultado.set("Error")       # si no se ingresa un número

# ---- Ventana principal ----
ventana = tk.Tk()
ventana.title("Calculadora básica")
ventana.geometry("250x180")

# ---- Variable para mostrar resultado ----
resultado = tk.StringVar()

# ---- Widgets (textos, cajas, botones) ----
tk.Label(ventana, text="Número 1:").pack()
entrada1 = tk.Entry(ventana)
entrada1.pack()

tk.Label(ventana, text="Número 2:").pack()
entrada2 = tk.Entry(ventana)
entrada2.pack()

tk.Button(ventana, text="Sumar", command=sumar).pack(pady=5)

tk.Label(ventana, text="Resultado:").pack()
tk.Label(ventana, textvariable=resultado, fg="blue").pack()

# ---- Bucle principal ----
ventana.mainloop()
