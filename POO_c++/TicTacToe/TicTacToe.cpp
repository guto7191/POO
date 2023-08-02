#include <iostream>
#include "TicTacToe.h"

using namespace std;

#define SIZE 3

TicTacToe::TicTacToe()
{
    iniciarArray();
}

void TicTacToe::marcarJogada(int linha, int coluna, char marcador)
{
    int valor_i, valor_j, test;
    bool sent_i, sent_j;

    sent_i = validarJogada(linha);
    sent_j = validarJogada(coluna);
    
    while(!sent_i)
    {
        cout << "Valor linha inválido forneça outro: ";
        cin >> test;
        sent_i = validarJogada(test);
    }

    valor_i = test; 
    
    test = 0; 

    while(!sent_j)
    {
        cout << "Valor coluna inválido forneça outro: ";
        cin >> test;
        sent_j = validarJogada(test);
    }
    valor_j = test;

    array[valor_i][valor_j] = (marcador == 'x') ? 1 : 0; 

}

void TicTacToe::iniciarArray()
{
    for(int i = 0; i < 3; i++){
        for(int j = 0; j < 3; j++){
            array[i][j] = 0;
        }
    }
}

bool TicTacToe::validarJogada(int valor)
{
    bool sent;

    sent = (1 <= valor && valor <= 3) ? true : false;
    
    return sent;   
}

void TicTacToe::printTabuleiro()
{
    cout << array[0][0] << "|"<< array[0][1] << "|" << array[0][2] << endl;
    cout<<"-------"<<endl;
    cout << array[1][0] << "|"<< array[1][1] << "|" << array[1][2] << endl;
    cout<<"-------"<<endl;
    cout << array[2][0] << "|"<< array[2][1] << "|" << array[2][2] << endl; 
    cout<<endl;
}

bool TicTacToe::checarLinha()
{
    return false;
}

bool TicTacToe::checarColuna()
{
    return false;
}

bool TicTacToe::checarVelha()
{
    return false;
}

bool TicTacToe::fimDeJogo()
{
    return false;
}
