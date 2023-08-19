class Jogador:


    def __init__(self, nome: str) -> None:
        self.nome = nome

    def marcar_posicao(self):
        var = input(f"Escolha a sua posição {self.get_nome()}: ")
        self.validar_posicao(var)
        #self.passar_posicao_para_tabuleiro
    

    def repitir_marcar_posicao(self):
        var = input(f"Valor inválido escolha a sua posição {self.get_nome()}: ")
        while var != 'x' and var != 'o':
            var = int(input(f"Valor inválido escolha a sua posição {self.get_nome()}: "))


    def validar_posicao(self, valor: str):
        # melhorar isso depois
        if valor != 'x' and valor != 'o':
            print("Valor Inválido!")
            self.repitir_marcar_posicao()


    def get_nome(self):
        return self.nome
