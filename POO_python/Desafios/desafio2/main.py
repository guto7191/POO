from dado import Dado
from pessoa import Pessoa
from jogo import Jogo

dado_6 = Dado()
dado_6.set_numero_de_faces(6)

jogador_1 = Pessoa("João", dado_6)
jogador_2 = Pessoa("Maria", dado_6)

jogar_dado = Jogo(jogador_1, jogador_2, dado_6)

jogar_dado.fazer_jogada()
