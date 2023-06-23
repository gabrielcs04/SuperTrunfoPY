from classes.cachorro import Cachorro
from classes.dinossauro import Dinossauro
from classes.jogo import Jogo
from utils.enum import TipoCarta, ModoJogo


escolha_tipo_carta = ""
while (escolha_tipo_carta != "C" and escolha_tipo_carta != "D"):
    print("Escolha com que tipo de carta você deseja jogar")
    escolha_tipo_carta = input("Cachorro (C) || Dinossauro (D): ").upper()
tipo_carta = TipoCarta.CACHORRO if (escolha_tipo_carta == "C") else TipoCarta.DINOSSAURO

escolha_modo_jogo = ""
while (escolha_modo_jogo != "N" and escolha_modo_jogo != "R"):
    print("Escolha com que tipo de carta você deseja jogar")
    escolha_modo_jogo = input("Noramal (N) || Reverso (R): ").upper()
modo_jogo = ModoJogo.NORMAL if (escolha_modo_jogo == "N") else ModoJogo.REVERSO

jogo = Jogo(tipo_carta, modo_jogo)
cartas_usuario, cartas_maquina = jogo.embaralhar_cartas()

print(cartas_usuario[0].nome)
print(cartas_maquina[0].nome)