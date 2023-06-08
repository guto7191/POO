#include <string>
using std::string; 

#ifndef CREAT_H
#define CREAT_H

class CreatAndDestroy
{
    public:
        CreatAndDestroy(int, string); //Construtor 
        ~CreatAndDestroy(); // Destrutor
    
    private:
        int objID;
        string message;
};

#endif
