#ifndef EMPLOYEE_H
#define EMPLOYEE_H

#include "Data.h"

class Employee
{
    public:
        Employee(const char * const,  const char * const, const Data &, const Data &);
        void print() const;
        ~Employee();

    private:
        char firstName[25];
        char lastName[25];
        Data birthData;
        const Data hireData;
};


#endif