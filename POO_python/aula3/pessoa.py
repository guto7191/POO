class Pessoa: 
    
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = self.validar_idade(idade)

    def get_idade(self) -> int:
        return self.idade

    def validar_idade(self, idade: int) -> int:
        if idade > 0:
            return idade
        else:
            return 1

    def get_nome(self) -> str:
        return self.nome

    def apresentar_idade(self) -> int:
        return self.get_idade()
    
    def informar_nome(self) -> str:
        return self.get_nome()



pessoa1 = Pessoa("Paulo", -15)

idade = pessoa1.apresentar_idade()
nome = pessoa1.informar_nome()

print(f"Nome = {nome} | Idade = {idade}")