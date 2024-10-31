import tkinter as tk
from tkinter import ttk
from clasePlantas import ControladorRegistros  # Asegúrate de que esta clase esté definida correctamente

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Registros de Plantas")
        self.geometry("800x500")
        self.resizable(False, False)  # Evita el redimensionamiento de la ventana

        # Instancia del controlador
        self.controlador = ControladorRegistros()

        # Crear widgets de la interfaz
        self.crear_widgets()

    def crear_widgets(self):
        frame = tk.Frame(self)
        frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Entrada de búsqueda
        self.entrada_busqueda = tk.Entry(frame, width=30)
        self.entrada_busqueda.grid(row=0, column=0, padx=5, pady=10, sticky="w")

        boton_buscar = tk.Button(frame, text="Buscar", command=self.buscar_registro)
        boton_buscar.grid(row=0, column=1, padx=5, pady=10, sticky="w")

        boton_obtener = tk.Button(frame, text="Obtener Registros", command=self.obtener_registros)
        boton_obtener.grid(row=0, column=2, padx=5, pady=10, sticky="w")

        # Crear tabla
        columnas = ("ID", "Nombre", "Apellido", "Ciudad", "Calle")
        self.tabla = ttk.Treeview(frame, columns=columnas, show="headings")
        self.tabla.grid(row=1, column=0, columnspan=3, sticky="nsew")

        for col in columnas:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, anchor="center", width=150)

        # Scrollbar
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=1, column=3, sticky="ns")

        # Etiqueta para mensajes
        self.resultado_label = tk.Label(frame, text="", font=("Arial", 10))
        self.resultado_label.grid(row=2, column=0, columnspan=3, pady=10)

        # Configurar expansión para que la tabla se ajuste al redimensionar la ventana
        frame.grid_rowconfigure(1, weight=1)  # Permite que la tabla se expanda
        frame.grid_columnconfigure(0, weight=1)  # Permite que el marco se expanda

