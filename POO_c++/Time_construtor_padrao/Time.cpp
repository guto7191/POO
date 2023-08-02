#include <iostream>

using namespace std;

#include "Time.h"
#include <iomanip>
using std::setfill;
using std::setw;


Time::Time(int hour, int minute, int second)
{
    setTime(hour,minute,second);
}

void Time::setTime(int hour, int minute, int second)
{
    setHour(hour);
    setMinute(minute);
    setSecond(second);
}


void Time::setHour(int valor)
{
    hour = (valor >= 0 && valor < 24) ? valor : 0;
}

void Time::setMinute(int valor)
{
    minute = (valor >= 0 && valor < 60) ? valor : 0;
}

void Time::setSecond(int valor)
{
     second = (valor >= 0 && valor < 60) ? valor : 0;
}

int Time::getHour()
{
    return hour;
}

int Time::getMinute()
{
    return minute;
}

int Time::getSecond()
{
    return second;
}

void Time::printUniversal()
{
    cout << setfill('0') << setw(2) << getHour() << ':' << setw(2) << getMinute() << ':' 
    << setw(2) << getSecond();
}
void Time::printStandard()
{
    cout << ((getHour() == 12 || getHour() == 0 )? 12 : getHour()%12) << ':' << setfill('0') 
    << setw(2) << getMinute() << ':' << setw(2) << getSecond() << (hour < 12 ? "AM" : "PM") <<endl;  

}