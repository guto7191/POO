#include <iostream>
#include "Time.h"

using namespace std;


Time::Time(int h, int m)
{
    setHour(h);
    sertMinute(m);
}

Time Time::operator+(const Time & tempo) const
{
    return ;
}

Time Time::operator+(int num) const
{
    return ;
}


void Time::setHour(int h)
{
     hour = ((0 > h) ? h : 0);
}

void Time::sertMinute(int m)
{
     hour = ((0 > m) ? m : 0);
}

// Função amiga é uma função externa ao escopa da classe
Time operator+(int num, const Time & t)
{
    Time soma;

    soma.hour = num + t.hour;
    soma.minute = t.minute;
    
    return soma; 
}