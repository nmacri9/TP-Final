class Carta:
    def __init__(self, valoracion:str, palo:str) -> None:
        self.valoracion = valoracion
        self.palo = palo
        self.valor_truco = self.obtener_valor_truco()
        self.valor_envido = self.obtener_valor_envido()

    def obtener_valor_truco(self):
        valores_truco = {
    '1': {'Espada': 14, 'Basto': 13, 'Oro': 8, 'Copa': 7},  
    '7': {'Espada': 12, 'Oro': 11, 'Basto': 6, 'Copa': 5},  
    '3': {'Espada': 10, 'Oro': 10, 'Copa': 10, 'Basto': 10},  
    '2': {'Espada': 9, 'Oro': 9, 'Copa': 9, 'Basto': 9},   
    '5': {'Espada': 4, 'Oro': 4, 'Copa': 4, 'Basto': 4},  
    '6': {'Espada': 3, 'Oro': 3, 'Copa': 3, 'Basto': 3},   
    '10': {'Espada': 7, 'Oro': 7, 'Copa': 7, 'Basto': 7},   
    '12': {'Espada': 7, 'Oro': 7, 'Copa': 7, 'Basto': 7},
}
        return valores_truco.get(self.valoracion, 0)

    def obtener_valor_envido(self):
        """Devuelve el valor de envido de la carta."""
        if self.valoracion in ['10', '11', '12']:
            return 0
        return int(self.valoracion)

    def __repr__(self) -> str:
        return f'{self.valoracion} de {self.palo}'

def cargar_cartas_desde_txt():
    """Carga las cartas desde un archivo de texto."""
    cartas = []
    with open("cartas.txt", 'r') as archivo:
        for linea in archivo:
            linea = linea.strip()  # el strip elimina espacios y saltos de línea
            if linea:  
                valoracion, palo = linea.split(' ')  # el strip separa el valor de la carta y el palo
                cartas.append(Carta(valoracion, palo))  
    return cartas

