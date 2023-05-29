#include <iostream>

using namespace std;
using std::endl;

#include "Time.h"


int main()
{
    Time t; 

    cout << "Incial Universal Time:";
    t.printUniversal();
    cout << "\nIncial Standard Time";
    t.printStandard();

    t.setTime(13,50,49);
    
    cout << "\nModificado Universal Time:";
    t.printUniversal();
    cout << "\nModificado Standard Time";
    t.printStandard();

    t.setTime(100,100,100);

    cout << "\nModificado Universal Time:";
    t.printUniversal();
    cout << "\nModificado Standard Time";
    t.printStandard();
    cout<<endl; 

    return 0;
}