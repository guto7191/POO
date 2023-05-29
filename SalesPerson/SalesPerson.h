// Definição da Classe SalesPerson

#ifndef SALESP_H
#define SALESP_H

class SalesPerson
{
public:
    SalesPerson();
    void getSalesFromUSer();
    void setSales(int, double);
    void printAnnualSales();

private:
    double totalAnnualSales();
    double sales[12];
};

#endif
