from typing import Type
from tabuleiro import Tabuleiro

class JogoDaVelha:

    def __init__(self, jogador_1: Type[Jogador], jogador_2: Type[Jogador]) -> None:
        self.tabuleiro = Tabuleiro()
    