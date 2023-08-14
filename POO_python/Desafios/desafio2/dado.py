import random 

class Dado:
    def __init__(self) -> None:
        self.__num_de_faces = 0
    
    def determinar_face(self) -> int:
        seed = random.randint(1, self.__num_de_faces)
        return seed 
    
    def set_numero_de_faces(self, valor):
        if valor <= 1:
            print("Erro")
        else:
            self.__num_de_faces = valor 


