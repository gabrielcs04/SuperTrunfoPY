from random import sample

from utils.enum import TipoCarta, ModoJogo
from classes.baralho import Baralho

class Jogo():
    cartas_usuario = []
    cartas_maquina = []
    
    def __init__(self, tipo_carta: TipoCarta, modo_jogo: ModoJogo) -> None:
        self.tipo_carta = tipo_carta
        self.modo_jogo = modo_jogo
        
    def embaralhar_cartas(self) -> list:
        cartas = Baralho().pegar_cartas(self.tipo_carta)
        
        indices_cartas = sample(range(32), 32)
        for i in range(32):
            if (i < 16):
                self.cartas_usuario.append(cartas[indices_cartas[i]])
            else:
                self.cartas_maquina.append(cartas[indices_cartas[i]])
    
    def mostrar_carta(self) -> None:
        carta_atual = self.cartas_usuario[0]
        carta_atual.mostrar_carta()