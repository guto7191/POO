class Tabuleiro:

    def __init__(self):
        self.matrix = [[0,0,0],[0,0,0],[0,0,0]]


    def print_tabuleiro(self):
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
