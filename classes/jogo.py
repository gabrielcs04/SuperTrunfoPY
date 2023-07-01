from random import sample

from utils.enum import TipoCarta, ModoJogo, ClasseCarta
from classes.baralho import Baralho

class Jogo():
    TOTAL_CARTAS = 32
    cartas_usuario = []
    cartas_maquina = []
    cartas_empates = []
    
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
        
        while not self.fim_de_jogo():
            self.iniciar_rodada()
            
        self.mostrar_resultado()

    def iniciar_rodada(self):
        print("-"*20, f"Sua pontuação: {self.pontos_usuario} || Pontuação da máquina: {self.pontos_maquina}", "-"*20)
        
        self.carta_usuario_atual = self.cartas_usuario[0]
        self.carta_maquina_atual = self.cartas_maquina[0]
        
        self.carta_usuario_atual.mostrar_carta()
        self.carta_maquina_atual.mostrar_carta()
        
        if (not self.tem_super_trunfo()):
            atributo = self.escolher_atributo()
            resultado = self.comparar_cartas(atributo)
        else:
            resultado = self.comparar_classes()
        self.resultado_rodada(resultado)
    
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

    def comparar_cartas(self, atributo: int) -> int:
        return self.carta_usuario_atual.comparar_carta(atributo, self.carta_maquina_atual, self.modo_jogo)

    def resultado_rodada(self, resultado: int) -> None:
        if (len(self.cartas_maquina) > 0 and len(self.cartas_usuario) > 0):
            primeira_carta_usuario = self.cartas_usuario.pop(0)
            primeira_carta_maquina = self.cartas_maquina.pop(0)
        
        if (resultado == 0):
            if (len(self.cartas_maquina) > 0 and len(self.cartas_usuario) > 0):
                self.cartas_empates.append(primeira_carta_usuario)
                self.cartas_empates.append(primeira_carta_maquina)
            else:
                self.cartas_usuario.append(primeira_carta_usuario)
                self.cartas_maquina.append(primeira_carta_maquina)
            print("\nOPS... DEU EMPATE NESSA RODADA\n")
        else:
            if (resultado == -1):
                self.cartas_maquina.append(primeira_carta_usuario)
                self.cartas_maquina.append(primeira_carta_maquina)
                self.cartas_maquina.extend(self.cartas_empates)
                print("\nQUE PENA... VOCÊ PERDEU ESSA RODADA\n")
            elif (resultado == 1):
                self.cartas_usuario.append(primeira_carta_maquina)
                self.cartas_usuario.append(primeira_carta_usuario)
                self.cartas_usuario.extend(self.cartas_empates)
                print("\nBOA... VOCÊ GANHOU ESSA RODADA\n")
            self.cartas_empates = []
        
        self.pontos_usuario = len(self.cartas_usuario)
        self.pontos_maquina = len(self.cartas_maquina)
    
    def tem_super_trunfo(self) -> bool:
        return (self.carta_usuario_atual.classe == ClasseCarta.SUPER_TRUNFO or self.carta_maquina_atual.classe == ClasseCarta.SUPER_TRUNFO)
    
    def comparar_classes(self) -> int:
        if (self.carta_usuario_atual.classe == ClasseCarta.SUPER_TRUNFO):
            if (self.carta_maquina_atual.classe == ClasseCarta.AA):
                print("\nSua carta atual é o SUPER TRUNFO, mas carta da máquina é do tipo AA, então ela venceu")
                return -1
            else:
                print("\nSua carta atual é o SUPER TRUNFO, então você venceu")
                return 1
        elif (self.carta_maquina_atual.classe == ClasseCarta.SUPER_TRUNFO):
            if (self.carta_usuario_atual.classe == ClasseCarta.AA):
                print("\nA carta atual da máquina é o SUPER TRUNFO, mas sua carta é do tipo AA, então você venceu")
                return 1
            else:
                print("\nA carta atual da máquina é o SUPER TRUNFO, então ela venceu")
                return -1
    
    def mostrar_resultado(self) -> None:
        if (self.pontos_usuario > self.pontos_maquina):
            print(f"Parabéns jogador(a)! Você ganhou do computador.")
        else:
            print(f"Poxa que pena... Você perdeu do computador.")
            
    def fim_de_jogo(self) -> bool:
        if (len(self.cartas_maquina) == 0 or len(self.cartas_usuario) == 0):
            return True
        return False
            
        