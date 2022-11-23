#include <iostream>
#include <vector>
#include <fstream>
#include "polyvect.cpp"

using namespace std;

int main()
{
    int n;
    double x[100];
    double y[100];
    cout << "How many data points?\n";
    cin >> n;
    for(int i=0;i<n;i++)
    {
        cout << "Enter (x,y) pair (" << i << ")\n";
        cin >> x[i];
        cin >> y[i];
    }
    vector<double> lagrange{0};
    for(int i=0;i<n;i++)
    {
        vector<double> poly;
        poly.push_back(1);
        double prod = 1;  
        for(int j=0;j<n;j++)
        {
            if(i==j)
                continue;
            else
            {
                prod = prod*(x[i]-x[j]);
                vector<double> expr {1, -x[j]};
                poly = mulexpr(poly,expr);
            }
        }
        prod = y[i]/prod;
        poly = coeffexpr(poly, prod);
        lagrange = addexpr(lagrange, poly);
    }
    printCoeffs(lagrange);
    ofstream coef("coefficients.txt");
    ofstream cords("coordinates.txt");
    cords << n << '\n';
    for(int i=0;i<lagrange.size();i++)
        cords << x[i] << ' ' << y[i] << '\n';
    for(int i=0;i<lagrange.size();i++)
        coef << lagrange[i] << ' ';
    coef.close();
    cords.close();
    system("pause");
    return 0;
}