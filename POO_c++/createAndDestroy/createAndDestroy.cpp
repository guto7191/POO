#include <iostream>
#include "createAndDestroy.h"

using namespace std;


CreatAndDestroy::CreatAndDestroy(int ID, string message)
{
    objID = ID;
    message = message;
    cout << "ObjID " << objID << "  Contrutor run   " << message << endl;
}

CreatAndDestroy::~CreatAndDestroy()
{
    cout << (objID == 1 || objID == 6 ? '\n' : ' ');
    cout<< "ObjID "<< objID << "  Destructor run   "<< message << endl; 
}