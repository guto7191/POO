from typing import Type
from dado import Dado
from pessoa import Pessoa 

class Jogo:

    def __init__(self, pessoa_1: Type[Pessoa], pessoa_2: Type[Pessoa], dado: Type[Dado]):
        self.__pessoa_1 = pessoa_1
        self.__pessoa_2 = pessoa_2
        self.__dado = dado

    
    def fazer_jogada(self):
        jogador_1 = self.__pessoa_1.jogar_dado()
        jogador_2 = self.__pessoa_2.jogar_dado()
        
        self.analisar_vencedor(jogador_1,jogador_2)

    def analisar_vencedor(self, jogador_1: int, jogador_2: int) -> None:
        if jogador_1 > jogador_2:
            self.print_estado_do_jogo(1)
        elif jogador_1 < jogador_2:
            self.print_estado_do_jogo(2)
        else:
            self.print_estado_do_jogo() 

    def print_estado_do_jogo(self, estado = 0) -> None:
        if estado == 1:
            print(f"O jogador {self.__pessoa_1.get_nome()} venceu !!")
        elif estado == 2:
            print(f"O jogador {self.__pessoa_2.get_nome()} venceu !!")
        else:
            print("Empate!!!")
    



        