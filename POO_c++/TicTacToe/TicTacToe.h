#ifndef TICTACTOE_H
#define TICTACTOE_H

class TicTacToe
{

public:
    TicTacToe();
    void jogador1(int);
    void jogador2(int); 
    void marcarJogada(int, int, char marcador);
    bool fimDeJogo();
    void printTabuleiro();

private:

    int array[3][3];
    int jogadas;
    bool checarLinha();
    bool checarColuna();
    bool checarVelha();
    void iniciarArray();
    bool validarJogada(int);
};

#endif
