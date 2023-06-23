import json

from utils.enum import TipoCarta
from classes.cachorro import Cachorro
from classes.dinossauro import Dinossauro


class Baralho():
    def pegar_cartas(self, tipo_carta: TipoCarta):
        cartas = []
        if (tipo_carta.CACHORRO):
            with open("utils/cachorros.json", encoding='utf-8') as arquivo:
                cachorros = json.load(arquivo)
            for c in cachorros:
                cartas.append(
                    Cachorro(
                        c["nome"], 
                        c["peso"], 
                        c["brincalhao"], 
                        c["agressividade"], 
                        c["obediencia"]
                    )
                )
        elif (tipo_carta.DINOSSAURO):
            with open("utils/dinossauros.json", encoding='utf-8') as arquivo:
                dinossauros = json.load(arquivo)
            for d in dinossauros:
                cartas.append(
                    Dinossauro(
                        d["nome"], 
                        d["peso"], 
                        d["altura"], 
                        d["comprimento"], 
                        d["viveu_ha"]
                    )
                )
        return cartas
