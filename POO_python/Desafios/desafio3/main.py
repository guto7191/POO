from jogo_da_velha import JogoDaVelha
from jogador import Jogador

jogador_1 = Jogador("Pedro")
jogador_2 = Jogador("Luiz")

jogo = JogoDaVelha(jogador_1, jogador_2)

jogo.pegar_jogada()