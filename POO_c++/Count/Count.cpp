#include <iostream>

using namespace std;


class Count
{
public:
    
    void setX(int value){
        x = value;
    }

    void print(){
        cout << x << endl;
    }

private:  
    int x;
};

int main()
{
    Count counter; //  Objeto do tipo Counter
    Count *counterPtr = &counter; // Ponteterio para um objeto do tipo Counter
    Count &counterRef = counter; // Uma referênia para um objeto do tipo Counter

    counter.setX(10);
    counter.print();
    cout << "------------------------" << endl;
    counterRef.setX(20);
    counterRef.print();
    cout << "------------------------" << endl;
    counterPtr->setX(30);
    counterPtr->print();
    
    return 0;
}
