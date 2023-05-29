#include <iostream>

using namespace std;
using std::fixed;

#include <iomanip>

using std::setprecision;

#include "SalesPerson.h"

// O construtor inicializa o vetor com 0.0
SalesPerson::SalesPerson(){
    for(int i = 0; i<12; i++){
        sales[i] = 0.0;
    }
}

// Ira pedir para o usuário entrar com os valores das vendas em cada mÊs
void SalesPerson::getSalesFromUSer()
{
    double salesFigure;
    for (int i = 1; i <= 12; i++){
        cout << "Digite o valor das vendas para o mês " << i << ': '; 
        cin >> salesFigure; 
        setSales(i,salesFigure);
    }
}

// Salva o valor das vendas do mês no vetor sales. Primeiramente verifica se os valores são válidos
void SalesPerson::setSales(int mont, double amount)
{
    if(mont >= 1 && mont <= 12 && amount > 0){
        sales[mont-1] = amount;
    }else
        cout << "Mês inválido ou valor menor que zero!\n";
}


// Mostra o valor total de vendas no ano
void SalesPerson::printAnnualSales()
{
    cout << setprecision(2) << fixed << "\nO total anual foi :" << totalAnnualSales() << endl ;
}

// Soma todos os valores presente do vetor sales e retorna um double
double SalesPerson::totalAnnualSales()
{
    double totalSales = 0;

    for(int i = 0; i < 12; i++){
        totalSales += sales[i];
    }
    return totalSales;
}



