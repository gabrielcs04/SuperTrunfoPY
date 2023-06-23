from utils.enum import TipoCarta, ModoJogo
from classes.baralho import Baralho
from random import sample

class Jogo():
    def __init__(self, tipo_carta: TipoCarta, modo_jogo: ModoJogo) -> None:
        self.tipo_carta = tipo_carta
        self.modo_jogo = modo_jogo
        
    def embaralhar_cartas(self) -> list:
        cartas = Baralho().pegar_cartas(self.tipo_carta)
        
        cartas_usuario = []
        cartas_maquina = []
        
        indices_cartas = sample(range(32), 32)
        for i in range(32):
            if (i < 16):
                cartas_usuario.append(cartas[indices_cartas[i]])
            else:
                cartas_maquina.append(cartas[indices_cartas[i]])
        
        return [cartas_usuario, cartas_maquina]
                