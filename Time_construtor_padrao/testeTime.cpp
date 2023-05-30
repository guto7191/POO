#include <iostream>
#include "Time.h"

using namespace std;

void print(const Time[],int);

int main(){
    int size = 5;
    Time t1;
    Time t2(10);
    Time t3(13,5);
    Time t4(12,23,58);
    Time t_invalided(60,65,90); 

    Time vetor[size] = {t1, t2, t3, t4, t_invalided}; 

    print(vetor,size);

    return 0;
}


void print(const Time tempos[], int size)
{
    Time t;

    for(int i = 0; i<size; i++)
    {
        t = tempos[i];
        cout<<"Valor em Horas\n";
        t.printUniversal();
        cout << endl;
        t.printStandard();
    }
}