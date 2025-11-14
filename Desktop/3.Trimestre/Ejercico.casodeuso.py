import tkinter as tk  # Importamos Tkinter

# --- Lista de productos (nombre, precio, cantidad) ---
productos = [
    ["Pan", 1500, 30],
    ["Leche", 3000, 15],
    ["Huevos", 600, 50],
    ["Arroz", 2500, 20],
    ["Azúcar", 2000, 25]
]

# --- Función que se ejecuta al presionar el botón ---
def mostrar_productos():
    texto_resultado.delete("1.0", tk.END)  # Limpia el texto anterior
    texto_resultado.insert(tk.END, "Nombre\tPrecio\tCantidad\n")  # Encabezado
    texto_resultado.insert(tk.END, "-"*35 + "\n")  # Línea separadora
    
    # Recorremos la lista y mostramos cada producto
    for p in productos:
        nombre, precio, cantidad = p
        texto_resultado.insert(tk.END, f"{nombre}\t${precio}\t{cantidad}\n")

# --- Crear la ventana principal ---
ventana = tk.Tk()
ventana.title("Visualizador de Productos")
ventana.geometry("400x300")

# --- Etiqueta principal ---
titulo = tk.Label(ventana, text="Lista de Productos", font=("Arial", 14, "bold"))
titulo.pack(pady=10)

# --- Botón para mostrar los productos ---
boton_mostrar = tk.Button(ventana, text="Mostrar productos", command=mostrar_productos)
boton_mostrar.pack(pady=5)

# --- Cuadro de texto donde se mostrarán los productos ---
texto_resultado = tk.Text(ventana, width=40, height=10)
texto_resultado.pack(pady=10)

# --- Iniciar la aplicación ---
ventana.mainloop()
