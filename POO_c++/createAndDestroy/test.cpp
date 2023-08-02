#include <iostream>
#include "createAndDestroy.h"

using namespace std;

void creat(void);

CreatAndDestroy obj1(1,"Global");

int main()
{
    cout << "\nMain" <<endl;
    static CreatAndDestroy obj2(2,"Local => static main");
    
    creat();

    cout << "\nMain function: execution resumes" << endl;
    CreatAndDestroy obj4(4,"Local => main");

    return 0;
}


void creat(void)
{
    cout <<"\nCreat function: Executions Begins" << endl;
    CreatAndDestroy obj5(5,"Local => creat");
    static CreatAndDestroy obj6(6,"Local => static creat");
    CreatAndDestroy obj7(7,"Local => creat");
    cout <<"\nCreat Function: Execution ends" << endl;
}