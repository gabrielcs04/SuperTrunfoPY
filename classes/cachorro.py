from pandas import DataFrame

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
        atributos = f"{self.nome}||(1) Peso||(2) Brincalhão||(3) Agressividade||(4) Obediência".split("||")
        valores = [[f"Classe {self.classe.value}"], [f"{self.peso:.2f} Kg"], [f"{self.brincalhao}/10"], [f"{self.agressividade}/10"], [f"{self.obediencia}/10"]]

        print(DataFrame(data=valores, index=atributos, columns=".".split()))
    
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