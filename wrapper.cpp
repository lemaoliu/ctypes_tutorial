//#include<string>
#include <iostream>
using namespace std;

extern "C" void print_array(double* array, int N)
{
    for (int i=0; i<N; i++) 
        cout << i << " " << array[i] << endl;
}


