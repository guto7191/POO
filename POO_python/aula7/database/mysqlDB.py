class MysqlDB:

    def __init__(self):
        self.__conexao = "Mysql"
    
    def conectar(self):
        print(f"Conectando no {self.__conexao}")
        return self.__conexao
    
    def desconectar(self):
        print(f"Desconectando do {self.__conexao}")
        return self.__conexao

    