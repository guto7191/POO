from dado import Dado
from pessoa import Pessoa

dado_6 = Dado()
dado_6.set_numero_de_faces(6)

jogador_1 = Pessoa("João", dado_6)
jogador_1.jogar_dado()


#valor_face = dado_6.determinar_face()
#print(valor_face)