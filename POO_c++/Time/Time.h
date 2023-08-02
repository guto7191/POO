//   
//     Declarção da Classe Time

// Impede multipla inclusões de arquivos cabeçalho
# ifndef TIME_H 
# define TIME_H

// Definição da Classe Time 
class Time{
    public:     
        Time(); //Construtor da Classe 
        void setTime( int, int, int); //configura hora, minuto e segundo
        void printUniversal();  // imprime a hora no formato de data/hora universal
        void printStandard(); // imprime a hora no formato-padrão de data/hora
    private:
        int hour;   // 0 - 23 
        int minute; // 0 - 59
        int second; // 0 - 59

}; // Fim da classe Time 

# endif