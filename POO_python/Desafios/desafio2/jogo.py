from typing import Type
class Jogo:

    def __init__(self, pessoa: Type[Pessoa], dado: Type[Dado]):
        self.__pessoa = pessoa
        self.__dado = dado

    
    def fazer_jogada(self):
        