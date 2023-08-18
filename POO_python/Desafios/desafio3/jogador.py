class Jogador:


    def __init__(self, nome: str) -> None:
        self.nome = nome

    def marcar_posicao(self):
        var = int(input(f"Escolha a sua posição {self.get_nome()}: "))
        self.validar_posicao(var)
    

    def repitir_marcar_posicao(self):
        var = int(input(f"Valor inválido escolha a sua posição {self.get_nome()}: "))
        while var <= 0 and var < 9:
            var = int(input(f"Valor inválido escolha a sua posição {self.get_nome()}: "))


    def validar_posicao(self, valor: int):
        # melhorar isso depois
        if valor <= 0 and valor < 9:
            print("Valor Inválido!")
            self.repitir_marcar_posicao()


    def get_nome(self):
        return self.nome
