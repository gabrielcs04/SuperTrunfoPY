from utils.enum import ClasseCarta


class Dinossauro():
    def __init__(self, classe: ClasseCarta, nome: str, peso: float, altura: float, comprimento: int, viveu_ha: int) -> None:
        self.classe = classe
        self.nome = nome
        self.peso = peso
        self.altura = altura
        self.comprimento = comprimento
        self.viveu_ha = viveu_ha
    
    def mostrar_carta(self):
        print(f"{self.nome} - {self.classe.value}")
        print(f"Peso: {self.peso:.2f} Ton")
        print(f"Altura: {self.altura} m")
        print(f"Comprimento: {self.comprimento} m")
        print(f"Viveu há: {self.viveu_ha} milhões de anos")
