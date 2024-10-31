import tkinter as tk
from tkinter import ttk
import requests

# Variable global para almacenar los datos obtenidos de la API
data = []

# Función para obtener registros desde la API
def obtener_registros():
    try:
        url = "https://671be4232c842d92c381a57e.mockapi.io/plantas"
        response = requests.get(url)
        response.raise_for_status()  # Verifica si la solicitud fue exitosa
        global data
        data = response.json()  # Guarda los datos en la variable global

        # Imprimir los datos para verificar su estructura
        print("Datos obtenidos de la API:", data)

        if data:
            mostrar_tabla(data)  # Mostrar todos los registros
            resultado_label.config(text=f"Se obtuvieron {len(data)} registros en total.")
        else:
            resultado_label.config(text="No se encontraron registros.")
    except requests.exceptions.RequestException as e:
        resultado_label.config(text=f"Error al obtener los registros: {e}")
    except Exception as e:
        resultado_label.config(text=f"Error inesperado: {e}")

# Función para mostrar los registros en la tabla
def mostrar_tabla(registros):
    # Limpiar la tabla antes de agregar nuevos registros
    tabla.delete(*tabla.get_children())

    # Agregar cada registro a la tabla
    for registro in registros:
        tabla.insert(
            "", "end", values=(
                registro.get("id", "N/A"),
                registro.get("nombre", "N/A"),
                registro.get("apellido", "N/A"),
                registro.get("ciudad", "N/A"),
                registro.get("calle", "N/A"),
            )
        )

def buscar_registro():
    termino = entrada_busqueda.get().strip()

    if not termino:
        resultado_label.config(text="Por favor, ingresa un término de búsqueda.")
        return  # Salir si no se ingresa un término

    if data:
        print(f"Término buscado: {termino}")  # Depuración en la consola

        # Filtrar si el término es un ID (coincidencia exacta) o texto en otros campos
        resultados = [
            registro for registro in data if
            str(registro.get("id", "")) == termino or  # Búsqueda exacta por ID
            termino in registro.get("nombre", "") or
            termino in registro.get("apellido", "") or
            termino in registro.get("ciudad", "") or
            termino in registro.get("calle", "")
        ]

        print("Resultados encontrados:", resultados)  # Verificar en la consola

        if resultados:
            mostrar_tabla(resultados)
            resultado_label.config(text=f"Se encontraron {len(resultados)} coincidencias.")
        else:
            resultado_label.config(text="No se encontraron coincidencias. Verifica el término.")
    else:
        resultado_label.config(text="No hay datos disponibles. Presiona 'Obtener Registros'.")

# Configuración de la interfaz gráfica
app = tk.Tk()
app.title("Registros de Plantas")
app.geometry("800x500")
app.resizable(False, False)  # Hacer la ventana no redimensionable

# Crear un marco para organizar los widgets
frame = tk.Frame(app)
frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# Entrada de búsqueda y botón de búsqueda
entrada_busqueda = tk.Entry(frame, width=30)
entrada_busqueda.grid(row=0, column=0, padx=5, pady=10, sticky="w")

boton_buscar = tk.Button(frame, text="Buscar", command=buscar_registro)
boton_buscar.grid(row=0, column=1, padx=5, pady=10, sticky="w")

# Botón para obtener los registros desde la API
boton_obtener = tk.Button(frame, text="Obtener Registros", command=obtener_registros)
boton_obtener.grid(row=0, column=2, padx=5, pady=10, sticky="w")

# Crear tabla (Treeview) para mostrar los registros
columnas = ("ID", "Nombre", "Apellido", "Ciudad", "Calle")
tabla = ttk.Treeview(frame, columns=columnas, show="headings")
tabla.grid(row=1, column=0, columnspan=3, sticky="nsew")

# Configurar encabezados y ancho de columnas
for col in columnas:
    tabla.heading(col, text=col)
    tabla.column(col, anchor="center", width=150)

# Agregar barra de desplazamiento vertical para la tabla
scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tabla.yview)
tabla.configure(yscroll=scrollbar.set)
scrollbar.grid(row=1, column=3, sticky="ns")

# Etiqueta para mostrar mensajes o errores
resultado_label = tk.Label(frame, text="", font=("Arial", 10))
resultado_label.grid(row=2, column=0, columnspan=3, pady=10)

# Configurar expansión para que la tabla se ajuste al redimensionar la ventana
frame.grid_rowconfigure(1, weight=1)
frame.grid_columnconfigure(0, weight=1)

# Iniciar la aplicación
app.mainloop()
 