#ifndef DATA_H
#define DATA_H


class Data
{
    public:
        Data(int = 1,int = 1,int = 1900);
        void print() const;
        ~Data(); 
    
    private:
        int month;
        int day;
        int year;

        int checkDAy(int) const;

};


#endif