from random import sample

from utils.enum import TipoCarta, ModoJogo
from classes.baralho import Baralho

class Jogo():
    TOTAL_CARTAS = 32
    cartas_usuario = []
    cartas_maquina = []
    
    carta_usuario_atual = None
    carta_maquina_atual = None
    
    pontos_usuario = 0
    pontos_maquina = 0
    
    def __init__(self, tipo_carta: TipoCarta, modo_jogo: ModoJogo) -> None:
        self.tipo_carta = tipo_carta
        self.modo_jogo = modo_jogo
    
    def iniciar_jogo(self):
        self.embaralhar_cartas()
        self.pontos_usuario = len(self.cartas_usuario)
        self.pontos_maquina = len(self.cartas_maquina)
        
        while self.pontos_usuario > 0 and self.pontos_maquina > 0:
            self.iniciar_rodada()

    def iniciar_rodada(self):
        print("-"*20, f"Sua pontuação: {self.pontos_usuario} || Pontuação da máquina: {self.pontos_maquina}", "-"*20)
        
        self.carta_usuario_atual = self.cartas_usuario[0]
        self.carta_maquina_atual = self.cartas_maquina[0]
        
        self.carta_usuario_atual.mostrar_carta()
        atributo = self.escolher_atributo()
        resultado = self.comparar_cartas(atributo)
        
        self.pontos_usuario += resultado
        self.pontos_maquina -= resultado
        
        primeira_carta_usuario = self.cartas_usuario.pop(0)
        primeira_carta_maquina = self.cartas_maquina.pop(0)
        
        if (resultado == 0):
            self.cartas_usuario.append(primeira_carta_usuario)
            self.cartas_maquina.append(primeira_carta_maquina)
            print("\nOPS... DEU EMPATE NESSA RODADA")
        elif (resultado == -1):
            self.cartas_maquina.append(primeira_carta_usuario)
            self.cartas_maquina.append(primeira_carta_maquina)
            print("\nQUE PENA... VOCÊ PERDEU ESSA RODADA")
        elif (resultado == 1):
            self.cartas_usuario.append(primeira_carta_maquina)
            self.cartas_usuario.append(primeira_carta_usuario)
            print("\nBOA... VOCÊ GANHOU ESSA RODADA")
    
    def embaralhar_cartas(self) -> list:
        cartas = Baralho().pegar_cartas(self.tipo_carta)
        
        indices_cartas = sample(range(32), 32)
        for i in range(self.TOTAL_CARTAS):
            if (i < self.TOTAL_CARTAS/2):
                self.cartas_usuario.append(cartas[indices_cartas[i]])
            else:
                self.cartas_maquina.append(cartas[indices_cartas[i]])
    
    def escolher_atributo(self) -> int:
        atributo = 0
        while atributo < 1 or atributo > 4:
            atributo = int(input("Escolha um atributo dessa carta: "))
        return atributo

    def comparar_cartas(self, atributo):
        return self.carta_usuario_atual.comparar_carta(atributo, self.carta_maquina_atual, self.modo_jogo)