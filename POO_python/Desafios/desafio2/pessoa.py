from typing import Type
from dado import Dado

class Pessoa:

    def __init__(self, nome: str, dado: Type[Dado]):
        self.__nome = nome
        self.dado = dado


    def get_nome(self):
        return self.__nome
    
    def jogar_dado(self) -> int:
        face = self.dado.determinar_face()
        print(f"Jogador {self.get_nome()} tirou a face {face}")
        return face
    