#ifndef TIME_H
#define TIME_H

class Time
{
public: 
    // COntrutor padrão 
    Time(int = 0, int = 0, int = 0);
    // Métodos 
    void setTime(int,int,int);
    void setHour(int);
    void setMinute(int);
    void setSecond(int);
    void printUniversal();
    void printStandard();

    int getHour();
    int getMinute();
    int getSecond();

private:
    //Atributos
    int hour;
    int minute;
    int second;
};




#endif