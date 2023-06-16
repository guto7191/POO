#include <iostream>
#include <iomanip>
#include "Time.h"

using namespace std;
using std::setfill;
using std::setw;

Time::Time(int hour, int minute, int second)
{
    setTime(hour, minute, second);
}

void Time::setTime(int hour, int minute, int second)
{
    setHour(hour);
    setMinute(minute);
    setSecond(second);
}

void Time::setHour(int h)
{
    hour = (0 <= h && h < 24)? h : 0;
}

void Time::setMinute(int m)
{
    minute = (0 <= m && m < 60)? m : 0;

}
void Time::setSecond(int s)
{
    second = (0<= s && s < 60)? s : 0;    
}

int Time::getHour() const
{
    return hour; 
}

int Time::getMinute() const
{
    return minute;
}

int Time::getSecond() const
{
    return second;
}

void Time::printUniversal() const
{
    cout << setfill('0') << setw(2) << hour << ":" << setw(2) << minute << ":"
    << setw(2) << second; 
}

void Time::printStandard()
{
    cout << ((hour == 12 ||  hour == 0) ? 12 : hour % 12)
    <<":"<< setfill('0') << setw(2) << minute << ":" 
    << setw(2) << second << (hour < 12 ? "AM" : "PM"); 
}