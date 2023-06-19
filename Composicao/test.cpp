#include <iostream>

using namespace std;

#include "Employee.h"


int main()
{
    Data birth(5,1,2002);
    Data hire(5,5,2020);
    Employee maneger("Luiz","Augusto",birth,hire);

    cout<<endl;
    
    maneger.print();
    
    cout << "\nTeste com valor de data inválido:\n";
    Data lastDayOff( 14, 35, 1994 ); // mês e dia inválidos
    cout << endl;
    
    return 0;
}