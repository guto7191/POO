#include <iostream>
#include <cstring>
#include "Employee.h"
#include "Data.h"

using namespace std;


/*
Prefira listas de inicializadores de membro em vez de atribuir valores no corpo do 
construtor. Uma lista de inicializadores de membro inicializa diretamente os membros.
Membros const e membros do tipo de referência devem ser inicializados na lista de 
inicializadores de membro.
 */

Employee::Employee(const char * const first, const char * const last, const Data &dataOfBirth, 
const Data &dataOfHire)
: birthData( dataOfBirth ), hireData( dataOfHire )
{
    int length = strlen(first);
    length = (length < 25 ? length : 24);
    strncpy(firstName, first, length);
    firstName[length] = '\0';

    length = strlen(last);
    length = (length < 25 ? length : 24);
    strncpy(lastName, last, length);
    lastName[length] = '\0';

    cout << "Objeto empregado construido " 
    << firstName << " " << lastName << endl; 
}

void Employee::print() const
{
    cout << lastName << " ," << firstName << " Hired: ";
    hireData.print();
    cout << " Birthday: ";
    birthData.print();
    cout<<endl;
}

Employee::~Employee()
{
    cout << "Objeto empregado destruido: " 
    << lastName << ',' << firstName << endl;
}

