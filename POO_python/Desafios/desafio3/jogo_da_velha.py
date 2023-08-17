from typing import Type
from tabuleiro import Tabuleiro
from jogador import Jogador

class JogoDaVelha:

    def __init__(self, jogador_1: Type[Jogador], jogador_2: Type[Jogador]) -> None:
        self.tabuleiro = Tabuleiro()
        self.jogador_1 = jogador_1
        self.jogador_2 = jogador_2
    

    def pegar_jogada(self):
        self.tabuleiro.print_tabuleiro()
        self.jogador_1.marcar_posicao()
        self.jogador_2.marcar_posicao()