#include <iostream>
#include "Time.h"

using namespace std;



int main()
{
    Time wakeUp(6,45,0);
    const Time noon(12,0,0);

    wakeUp.setHour(12);
    wakeUp.getHour();

    noon.getMinute();
    noon.printUniversal();

    // Função não delcrada como const tentando acessar um objeto const retorna um erro
    //noon.printStandard()
}