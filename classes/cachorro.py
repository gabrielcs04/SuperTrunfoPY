from utils.enum import ClasseCarta, ModoJogo

class Cachorro():
    def __init__(self, classe: ClasseCarta, nome: str, peso: float, brincalhao: int, agressividade: int, obediencia: int) -> None:
        self.classe = classe
        self.nome = nome
        self.peso = peso
        self.brincalhao = brincalhao
        self.agressividade = agressividade
        self.obediencia = obediencia

    def mostrar_carta(self) -> None:
        print(f"{self.nome} - {self.classe.value}")
        print(f"(1) - Peso: {self.peso:.2f} Kg")
        print(f"(2) - Brincalhão: {self.brincalhao}/10")
        print(f"(3) - Agressividade: {self.agressividade}/10")
        print(f"(4) - Obediência: {self.obediencia}/10")
    
    def comparar_carta(self, atributo: int, outra_carta, modo_jogo: ModoJogo) -> int:
        if (modo_jogo == ModoJogo.NORMAL):
            if (atributo == 1):
                return 0 if (self.peso == outra_carta.peso) else -1 if (self.peso < outra_carta.peso) else 1
            elif (atributo == 2):
                return 0 if (self.brincalhao == outra_carta.brincalhao) else -1 if (self.brincalhao < outra_carta.brincalhao) else 1
            elif (atributo == 3):
                return 0 if (self.agressividade == outra_carta.agressividade) else -1 if (self.agressividade < outra_carta.agressividade) else 1
            elif (atributo == 4):
                return 0 if (self.obediencia == outra_carta.obediencia) else -1 if (self.obediencia < outra_carta.obediencia) else 1
        else:
            if (atributo == 1):
                return 0 if (self.peso == outra_carta.peso) else 1 if (self.peso < outra_carta.peso) else -1
            elif (atributo == 2):
                return 0 if (self.brincalhao == outra_carta.brincalhao) else 1 if (self.brincalhao < outra_carta.brincalhao) else -1
            elif (atributo == 3):
                return 0 if (self.agressividade == outra_carta.agressividade) else 1 if (self.agressividade < outra_carta.agressividade) else -1
            elif (atributo == 4):
                return 0 if (self.obediencia == outra_carta.obediencia) else 1 if (self.obediencia < outra_carta.obediencia) else -1