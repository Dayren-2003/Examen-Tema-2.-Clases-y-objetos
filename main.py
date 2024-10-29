import tkinter as tk
from tkinter import ttk
from clasePlantas import ControladorRegistros

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Registros de Plantas")
        self.geometry("800x500")

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

        # Configurar expansión
        frame.grid_rowconfigure(1, weight=1)
        frame.grid_columnconfigure(0, weight=1)

    def obtener_registros(self):
        data = self.controlador.obtener_registros()
        if data:
            registros = self.controlador.seleccionar_registros_aleatorios()
            self.mostrar_tabla(registros)
            self.resultado_label.config(text=f"Se obtuvieron {len(data)} registros en total.")
        else:
            self.resultado_label.config(text="Error al obtener los registros.")

    def buscar_registro(self):
        termino = self.entrada_busqueda.get().strip()
        if not termino:
            self.resultado_label.config(text="Por favor, ingresa un término de búsqueda.")
            return

        resultados = self.controlador.buscar_registro(termino)
        if resultados:
            self.mostrar_tabla(resultados)
            self.resultado_label.config(text=f"Se encontraron {len(resultados)} coincidencias.")
        else:
            self.resultado_label.config(text="No se encontraron coincidencias.")

    def mostrar_tabla(self, registros):
        self.tabla.delete(*self.tabla.get_children())
        for registro in registros:
            self.tabla.insert(
                "", "end", values=(
                    registro.get("id", "N/A"),
                    registro.get("nombre", "N/A"),
                    registro.get("apellido", "N/A"),
                    registro.get("ciudad", "N/A"),
                    registro.get("calle", "N/A"),
                )
            )

if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()