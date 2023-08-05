class Elevador:
    
    def __init__(self, quantidade_de_andares: int) -> None:
        self.quantidade_de_andares = quantidade_de_andares
        self.andar_atual = 1
            


    def subir(self, andar) -> None:
        if self.validar_andar(andar):
            self.realizar_calculo_de_distancia_subida(andar)
        else:
            print("Andar inválido!")



    def descer(self, andar: int) -> None:
        if self.validar_andar(andar):
            self.realizar_calculo_de_distancia_descida(andar)
        else:
            print("Andar inválido!")




    def print_andar(self):
        print(f"Andar: {self.andar_atual}")



    def validar_andar(self, andar: int) -> bool:
        if andar >= 1 and andar <= self.quantidade_de_andares and isinstance(andar, int):
            return True
        else:
            return False
    


    def realizar_calculo_de_distancia_subida(self, andar: int) -> None:
        distancia = (andar - self.andar_atual )
        self.andar_atual += distancia


    
    def realizar_calculo_de_distancia_descida(self, andar: int) -> None:
        distancia = (self.andar_atual - andar)
        self.andar_atual -= distancia