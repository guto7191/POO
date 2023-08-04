class Pessoa: 
    
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade


    def dirigir(self, veiculo: str) -> None:
        print(f{"Digindo {veiculo}"})

    def cantar(self) -> None:
        print("Cantando")

    def apresentar_idade(self) -> int:
        return self.idade
    