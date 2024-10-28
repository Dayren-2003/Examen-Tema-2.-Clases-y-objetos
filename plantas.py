import tkinter as tk
from tkinter import ttk  # Para usar Treeview
import requests


# Función para obtener todos los registros desde la API y mostrarlos en la tabla
def obtener_registros():
    try:
        url = "https://671be4232c842d92c381a57e.mockapi.io/plantas"
        response = requests.get(url)
        response.raise_for_status()  # Verifica si hubo un error en la solicitud
        data = response.json()

        print(data)  # Verificar si los datos se obtienen correctamente

        if data:
            mostrar_tabla(data)  # Mostrar todos los registros en la tabla
        else:
            resultado_label.config(text="No se encontraron registros.")
    except Exception as e:
        resultado_label.config(text=f"Error: {e}")


# Función para mostrar los registros en la tabla
def mostrar_tabla(data):
    # Limpiar la tabla antes de agregar nuevos datos
    for row in tabla.get_children():
        tabla.delete(row)

    # Agregar cada registro como una nueva fila en la tabla
    for registro in data:
        print(f"Agregando registro: {registro}")  # Debug para verificar los datos
        tabla.insert(
            "", "end", values=(
                registro.get("id", "N/A"),
                registro.get("nombre", "N/A"),
                registro.get("apellido", "N/A"),
                registro.get("ciudad", "N/A"),
                registro.get("calle", "N/A")
            )
        )


# Configuración de la interfaz gráfica
app = tk.Tk()
app.title("Registros Plantas")
app.geometry("800x400")

# Crear un marco para organizar los widgets
frame = tk.Frame(app)
frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# Botón para obtener los registros
boton = tk.Button(frame, text="Obtener Registros", command=obtener_registros)
boton.grid(row=0, column=0, pady=10)

# Crear tabla (Treeview)
columnas = ("ID", "Nombre", "Apellido", "Ciudad", "Calle")
tabla = ttk.Treeview(frame, columns=columnas, show="headings")
tabla.grid(row=1, column=0, sticky="nsew")

# Configurar encabezados y columnas de la tabla
for col in columnas:
    tabla.heading(col, text=col)
    tabla.column(col, anchor="center", width=100)

# Agregar barra de desplazamiento vertical
scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tabla.yview)
tabla.configure(yscroll=scrollbar.set)
scrollbar.grid(row=1, column=1, sticky="ns")

# Label para mostrar errores o mensajes
resultado_label = tk.Label(frame, text="", font=("Arial", 10))
resultado_label.grid(row=2, column=0, pady=10)

# Configurar expansión para que la tabla se ajuste al redimensionar la ventana
frame.grid_rowconfigure(1, weight=1)
frame.grid_columnconfigure(0, weight=1)

# Iniciar la aplicación
app.mainloop()
