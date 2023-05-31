#ifndef TICTACTOE_H
#define TICTACTOE_H

class TicTacToe
{

public:
    TicTacToe();
    void jogador1(int);
    void jogador2(int); 


private:

    int array[3][3];
    int jogadas;
    bool checarLinha();
    bool checarColuna();
    void iniciarArray();
};

#endif
