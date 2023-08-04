class Sistema:

    def cadastrar(self, nome: str, idade: int) -> None:
        if self.__validar_dados(nome, idade):
           self.__amazenar_dados(nome, idade)
        else:
            self.__indicar_erro()

    def __validar_dados(self, nome: str, idade: int) -> bool:
        if isinstance(idade, int) and idade > 0 and isinstance(nome, str):
            return True
        else: 
            return False
    
    def __amazenar_dados(self, nome: str, idade: int) -> None:
        print("Acessando banco de dados ...")
        print(f"Cadastrando usuário: {nome} | idade:  {idade}")    
    
    def __indicar_erro(self) -> None:
        print("Dados inválidos!")




sistema_de_cadastro = Sistema() 

sistema_de_cadastro.cadastrar("Luiz",15)
sistema_de_cadastro.cadastrar(15,"ola")