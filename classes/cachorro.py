from utils.enum import ClasseCarta


class Cachorro():
    def __init__(self, classe: ClasseCarta, nome: str, peso: float, brincalhao: int, agressividade: int, obediencia: int) -> None:
        self.classe = classe
        self.nome = nome
        self.peso = peso
        self.brincalhao = brincalhao
        self.agressividade = agressividade
        self.obediencia = obediencia

    def mostrar_carta(self):
        print(f"{self.nome} - {self.classe.value}")
        print(f"Peso: {self.peso:.2f} Kg")
        print(f"Brincalhão: {self.brincalhao}/10")
        print(f"Agressividade: {self.agressividade}/10")
        print(f"Obediência: {self.obediencia}/10")