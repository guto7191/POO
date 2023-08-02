#ifndef TIME_H
#define TIME_H


class Time
{
    public:
        Time(int = 0, int = 0);
        Time(int,int);
        friend Time operator+(int, const Time &);
        Time operator+(const Time &) const;
        Time operator+(int) const;
        void setHour(int);
        void sertMinute(int);

    private:
        int hour;
        int minute;

};



#endif