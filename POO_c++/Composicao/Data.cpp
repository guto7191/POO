#include <iostream>
#include "Data.h"

using namespace std;

Data::Data(int mn, int dy, int yr)
{
    if(1 <= mn && mn <= 12)
    {
        month = mn;
    }
    else
    {
        month = 1;
        cout<<"Mês inválido! Mês configurado por padrão para 1 "<<endl;
    }

    year = yr;
    day = checkDAy(dy);

    cout << "Obejto Data contruido para a data: ";
    print();
    cout << endl;
}


void Data::print() const
{
    cout << month << '/' << day << '/' << year << endl; 
}

Data::~Data()
{
    cout<< "Objeto Data destruido para a data: ";
    print();
    cout<<endl;
}

int Data::checkDAy(int dy) const
{
    static const int dayPerMonth[13] =
    {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

    if(1 <= dy && dy <= dayPerMonth[month])
        return dy;
    
    /*
    Um ano é bissexto se for:
        Divisível por 4 .
        Não é divisível por 100 .
        Divisível por 400 .
    */
    if(month == 2 && dy == 29 && (year % 400 == 0 ||
    (year % 4 == 0 && year % 100 != 0)))
        return dy;
    
    cout << "Dia inválido ! Definido como 1.";
        return 1;
}


