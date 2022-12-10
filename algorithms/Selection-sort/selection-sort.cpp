// this code generates an integer array of user-specified size and does selection-sort on it
#include<iostream>
#include<ctime>
using namespace std;

int least(int a[], int n, int j);   // function that returns the index of the least component in array
void swapp(int a[], int I, int j);  // function that swaps list[I] and list[j]
void print(int a[], int n);         // function that prints the array in a line

int main()
{
    int a1[30], a2[30]; // a1 = main list, a2 = temp list that is manipulated
    int n;              // size
    srand(time(0));

    // Specifying list length
    cout << "Size ?" << endl;
    cin >> n;
    cout << "Size of list = ", n;

    // initializing main list
    for (int k=0; k<n; k++)
        a1[k] = rand()%100;

    // assigning list to templist
    for (int k=0; k<n; k++)
        a2[k] = a1[k];

    // printing the list
    cout << "Array = ";
    print (a1,n);

    // sorting :
    cout << "\nSorting steps : " << endl;
    for (int j=0; j<n; j++)
    {
        cout << j+1 << ". ";
        swapp(a2, least(a2,n,j), j);
        print(a2,n);
    }
    return 0;
}

int least(int a[], int n, int j)
{
    int I=j;

    for (int i=j+1; i<n; i++)
    {
        if (a[I] > a[i])
            I=i;
    }
    return I;
}

void swapp(int a[], int I, int j)
{
    int temp;

    temp = a[j];
    a[j] = a[I];
    a[I] = temp;
}

void print(int a[], int n)
{
    for (int k=0; k<n; k++)
        cout << a[k] << " " ;
    cout << "\n";
}
