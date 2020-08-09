//write a program to print # pattern

#include <iostream>
using namespace std;
int main()
{
    int i,j,k;
    cout<<"enter the no. of rows = ";
    cin>>j;
    for(i=1;i<=j;i++)
    {
        for(k=1;k<=j;k++)
        {
            cout<<"# ";
        }
        cout<<"\n";

    }
    return 0;
}
