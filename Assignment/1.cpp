#include <iostream>     // this is a directive input output
using namespace std;    // using standard namespace
int main()                  // main function
{                           // open main function
    int num,i,j;                // declare numeric variable num, i and j
    cout << "This is a program to display a multiplication table" << endl;// display this is a program to display a multiplication table to the user
    cout << "Enter maximum limit:"; // display print maximum out put to the user
    cin >> num;         // accept number and store in num
    for (int i=1; i <=12; i++)      // condition if i=1, i smaller than or equal to 12 and i+1
    {                   // open for function
        for (j=1;j<=num; j++)   // condition if j=1, j smaller than or equal to num and j+1
        {               // open for function
            if (j <= num-1)
            {       // open if function
                cout << i*j << "\t";        // i*j
            }           // close if function
            else 
            {       // open else function
                cout << i*j<< "\t";     // i*j
            }       // close else function
        }       // close for function
        cout << endl;  // endline
    }       // close for function
    return 0; // return 0 to os
}       // close main function
