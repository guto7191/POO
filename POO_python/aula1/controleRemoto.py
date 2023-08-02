class ControleRemoto:

    def __init__(self, televisao, comodo):
        self.televisao = televisao
        self.comodo = comodo

    def avancar_canal(self):
        print("Canal avancado")
    
    def voltar_canal(self):
        print("Voltar canal")
    
    def escolher_canal(self, canal):
        print("Alterado para o canal: {}".format(cana))

    def getComodo(self):
        return self.comodo

    def getTelevisao(self):
        return self.televisao


controle_1 = ControleRemoto("Lg","sala")

print(controle_1.getComodo())
print(controle_1.getTelevisao())
controle_1.avancar_canal()
controle_1.voltar_canal()
