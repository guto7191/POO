class Interrupitor:

    def __init__(self, comodo: str):
        self.__comodo = comodo
    

    def acender(self):
        print(f"Acendendo {self.__comodo}")   
    
    def apagar(self):
        print(f"Apagando {self.__comodo}")