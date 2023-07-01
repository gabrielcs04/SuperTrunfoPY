from pandas import DataFrame

from utils.enum import ClasseCarta, ModoJogo

    
class Dinossauro():
    def __init__(self, classe: ClasseCarta, nome: str, peso: float, altura: float, comprimento: int, viveu_ha: int) -> None:
        self.classe = classe
        self.nome = nome
        self.peso = peso
        self.altura = altura
        self.comprimento = comprimento
        self.viveu_ha = viveu_ha
    
    def mostrar_carta(self) -> None:
        atributos = f"{self.nome}||(1) Peso||(2) Altura||(3) Comprimento||(4) Viveu há".split("||")
        valores = [[f"Classe {self.classe.value}"], [f"{self.peso:.2f} Kg"], [f"{self.altura} m"], [f"{self.comprimento} m"], [f"{self.viveu_ha} mi de anos"]]

        print(DataFrame(data=valores, index=atributos, columns=".".split()))
    
    def comparar_carta(self, atributo: int, outra_carta, modo_jogo: ModoJogo) -> int:
        if (modo_jogo == ModoJogo.NORMAL):
            if (atributo == 1):
                return 0 if (self.peso == outra_carta.peso) else -1 if (self.peso < outra_carta.peso) else 1
            elif (atributo == 2):
                return 0 if (self.altura == outra_carta.altura) else -1 if (self.altura < outra_carta.altura) else 1
            elif (atributo == 3):
                return 0 if (self.comprimento == outra_carta.comprimento) else -1 if (self.comprimento < outra_carta.comprimento) else 1
            elif (atributo == 4):
                return 0 if (self.viveu_ha == outra_carta.viveu_ha) else -1 if (self.viveu_ha < outra_carta.viveu_ha) else 1
        else:
            if (atributo == 1):
                return 0 if (self.peso == outra_carta.peso) else 1 if (self.peso < outra_carta.peso) else -1
            elif (atributo == 2):
                return 0 if (self.altura == outra_carta.altura) else 1 if (self.altura < outra_carta.altura) else -1
            elif (atributo == 3):
                return 0 if (self.comprimento == outra_carta.comprimento) else 1 if (self.comprimento < outra_carta.comprimento) else -1
            elif (atributo == 4):
                return 0 if (self.viveu_ha == outra_carta.viveu_ha) else 1 if (self.viveu_ha < outra_carta.viveu_ha) else -1
