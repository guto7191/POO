#include <iostream>
#include "Jogador.h"

using namespace std;


Jogador::Jogador(char caracter)
{
    setMarcador(caracter);
}


void Jogador::setMarcador(char caracter)
{
    marcador = caracter;
}

char Jogador::getMarcador()
{
    return marcador; 
}


