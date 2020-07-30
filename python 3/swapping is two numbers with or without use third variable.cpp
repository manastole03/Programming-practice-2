#include<iostream>
using namespace std;
int main()
//swapping by using third variable
/*{
    int a,b,t=0;
    cout<<"enter two numbers";
    cin>>a>>b;
    cout<<"numbers before swapping is %d   %d"<<a << b<<endl;
    t=a;
    a=b;
    b=t;
    cout<<"numbers after swapping is %d   %d"<<a << b<<endl;
}*/
//swapping without using third variable
{
    int a,b;
    cout<<"enter two numbers";
    cin>>a>>b;
    cout<<"numbers before swapping is %d \t %d"<<a <<b<<endl;
    a=a+b;
    b=a-b;
    a=a-b;
    cout<<"numbers after swapping is %d   %d"<<a <<b<<endl;
}
