import requests
import random

class ControladorRegistros:
    def __init__(self):
        self.__data = []  # Atributo privado para almacenar los datos

    def obtener_registros(self):
        """Obtiene registros desde la API y los guarda en el atributo privado."""
        try:
            url = "https://671be4232c842d92c381a57e.mockapi.io/plantas"
            response = requests.get(url)
            response.raise_for_status()
            self.__data = response.json()

            print("Datos obtenidos de la API:", self.__data)  # Depuración
            return self.__data  # Retorna los datos para su uso
        except requests.exceptions.RequestException as e:
            print(f"Error al obtener los registros: {e}")
            return None

    def seleccionar_registros_aleatorios(self, cantidad=10):
        """Selecciona una cantidad limitada de registros aleatorios."""
        if not self.__data:
            return []

        num_registros = min(len(self.__data), cantidad)
        return random.sample(self.__data, num_registros)

    def buscar_registro(self, termino):
        """Busca registros que coincidan con el término ingresado."""
        if not self.__data:
            print("No hay datos disponibles.")
            return []

        resultados = [
            registro for registro in self.__data if
            str(registro.get("id", "")).lower() == termino.lower() or
            termino.lower() in registro.get("nombre", "").lower() or
            termino.lower() in registro.get("apellido", "").lower() or
            termino.lower() in registro.get("ciudad", "").lower() or
            termino.lower() in registro.get("calle", "").lower()
        ]
        print("Resultados encontrados:", resultados)  # Depuración
        return resultados
