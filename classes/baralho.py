import json

from utils.enum import TipoCarta, ClasseCarta
from classes.cachorro import Cachorro
from classes.dinossauro import Dinossauro


class Baralho():
    
    def __definir_classe(self, classe: str) -> ClasseCarta:
        for enum_classe in ClasseCarta:
            if (enum_classe.value == classe.upper()):
                return enum_classe
    
    def pegar_cartas(self, tipo_carta: TipoCarta):
        cartas = []
        if (tipo_carta == TipoCarta.CACHORRO):
            with open("utils/cachorros.json", encoding='utf-8') as arquivo:
                cachorros = json.load(arquivo)
            for c in cachorros:
                cartas.append(
                    Cachorro(
                        self.__definir_classe(c["classe"]),
                        c["nome"], 
                        c["peso"], 
                        c["brincalhao"], 
                        c["agressividade"], 
                        c["obediencia"]
                    )
                )
        elif (tipo_carta == TipoCarta.DINOSSAURO):
            with open("utils/dinossauros.json", encoding='utf-8') as arquivo:
                dinossauros = json.load(arquivo)
            for d in dinossauros:
                cartas.append(
                    Dinossauro(
                        self.__definir_classe(d["classe"]),
                        d["nome"], 
                        d["peso"], 
                        d["altura"], 
                        d["comprimento"], 
                        d["viveu_ha"]
                    )
                )
        return cartas
