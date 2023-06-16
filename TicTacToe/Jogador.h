#ifndef JOGADOR_H
#define JOGADOR_

class Jogador
{
    public:
        Jogador(char);
        void setMarcador(char);
        char getMarcador();
        
    private:
        char marcador;

};


#endif