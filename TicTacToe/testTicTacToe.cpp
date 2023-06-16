#include <iostream>
#include "TicTacToe.h"
#include "Jogador.h"

using namespace std;


void loop(TicTacToe tabuleiro, Jogador player_x, Jogador player_o);
void jogada(TicTacToe,Jogador,Jogador);

int main()
{
    TicTacToe tabuleiro;
    Jogador player_x('x');
    Jogador player_o('o');

    loop(tabuleiro, player_x, player_o);
}


void jogada(TicTacToe tabuleiro, Jogador player)
{
    int linha, coluna;
    cout << "Digite a linha e a coluna:"<<endl;
    cin >> linha;
    cin >> coluna;
    tabuleiro.marcarJogada(linha, coluna, player.getMarcador());    

}

void loop(TicTacToe tabuleiro, Jogador player_x, Jogador player_o)
{
    bool fimDeJogo = false;
    int rodada = 0;
    tabuleiro.printTabuleiro();

    while(!fimDeJogo)
    {
        if(rodada % 2 == 0)
            jogada(tabuleiro,player_x);
        else
            jogada(tabuleiro, player_o);
        
        tabuleiro.printTabuleiro();
        
        rodada++;
        fimDeJogo = tabuleiro.fimDeJogo();
    }
}
