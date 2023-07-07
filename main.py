from classes.usuario import Usuario
from classes.jogo import Jogo
from utils.enum import TipoCarta, ModoJogo


print("=-"*15, "BEM-VINDO AO SUPER TRUNFO", "=-"*15)
print()

nome = str(input("Digite o seu nome: "))
sobrenome = str(input("Digite o seu sobrenome: "))
idade = int(input("Digite a sua idade: "))
apelido = str(input("Digite um apelido para usar durante o jogo: "))

usuario = Usuario(nome, sobrenome, idade, apelido)

print("\n", "-"*87, "\n")

escolha_tipo_carta = ""
while (escolha_tipo_carta != "C" and escolha_tipo_carta != "D"):
    escolha_tipo_carta = input("Escolha um tipo de carta -> Cachorro (C) || Dinossauro (D): ").upper()

tipo_carta = TipoCarta.CACHORRO if (escolha_tipo_carta == "C") else TipoCarta.DINOSSAURO

escolha_modo_jogo = ""
while (escolha_modo_jogo != "N" and escolha_modo_jogo != "R"):
    escolha_modo_jogo = input("Escolha o um modo de jogo -> Normal (N) || Reverso (R): ").upper()
modo_jogo = ModoJogo.NORMAL if (escolha_modo_jogo == "N") else ModoJogo.REVERSO

print()

jogo = Jogo(tipo_carta, modo_jogo)
jogo.iniciar_jogo()
