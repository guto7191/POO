class Jogador:


    def __init__(self, nome: str) -> None:
        self.nome = nome

    def marcar_posicao(self):
        var = int(input(f"Escolha a sua posição {self.get_nome()}: "))
        self.validar_posicao(var)


    def validar_posicao(self, valor: int) -> bool:
        # melhorar isso depois
        if valor <= 0 and valor > 9:
            print("Valor Inválido!")
            return False 
        else:
            return True

    def get_nome(self):
        return self.nome
