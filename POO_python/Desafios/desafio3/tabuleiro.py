class Tabuleiro:

    def __init__(self):
        self.matrix = [[" "," "," "],[" "," "," "],[" ", " ", " "]]
    
    def passar_posicao_para_tabuleiro(self, valor: str) -> None:
        pass 

    def print_tabuleiro(self):
        print("Tabuleiro!\n ")
        print(f"{self.matrix[0][0]} | {self.matrix[0][1]} | {self.matrix[0][2]}\n" + "_" * 10 + "\n" + 
        f"\n{self.matrix[1][0]} | {self.matrix[1][1]} | {self.matrix[1][2]}\n" + "_" * 10 + "\n" + 
        f"\n{self.matrix[2][0]} | {self.matrix[2][1]} | {self.matrix[2][2]}\n")

    ### Só de meme isso aqui hueheueheu
    def _print_tabuleiro(self):
        print("Tabuleiro!\n ")
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if (j != 2):
                    print(f"{self.matrix[i][j]} |", end=" ")      
                else:
                    print(self.matrix[i][j], end=" ")
            if(i!=2):
                print('\n' + '_'* 10 + '\n')
            else: 
                print("\n")
