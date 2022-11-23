#include <iostream>
#include <vector>

using namespace std;

double pow(double x,int n)
{
    double y=1;
    for(int i=0;i<n;i++)
    {
        y = y*x;
    }
    return y;
}

double getval(vector<double> c, double x)
{
    double xval=0;
    int n = c.size();
    for(int i=0;i<n;i++)
    {
        xval = xval+pow(x,(n-1)-i)*c[i]; 
    }
    return xval;
}

void printCoeffs(vector<double> c)
{
    int n = c.size();
    for(int i=0;i<n-1;i++)
    {
        cout << "Coefficient of x^" << (n-1)-i << " : " << c[i] << '\n';
    }
    cout << "Constant term : " << c[n-1] << '\n';
}

void print(vector<double> c)
{
    for(int i=0;i<c.size();i++)
        cout << c[i] << ' ';
    
}

int max(int a, int b)
{
    if(a>b)
        return a;
    else
        return b;
}
vector<double> pushzero(vector<double> v, int n)
{
    for(int i=0;i<n;i++)
        v.push_back(0);
    return v;
}

vector<double> coeffexpr(vector<double> v, double d)
{
    vector<double> v1;
    for(int i=0;i<v.size();i++)
    {
        v1.push_back(v[i]*d);
    }
    return v1;
}

vector<double> addexpr(vector<double> v1, vector<double> v2)
{
    vector<double> vadd; 
    if(v1.size()!=v2.size())
    {
        
        int n = max(v1.size(),v2.size());
        for(int i=0;i<(v1.size()+v2.size()-2*n);i++)
        {
            if(v1.size()!=n)
                v1.insert(v1.begin(),0);
            else
                v2.insert(v2.begin(),0);
        }
    }
    for(int i=0;i<v1.size();i++)
        vadd.push_back(v1[i]+v2[i]);
    return vadd;
}

vector<double> mulexpr(vector<double> v1, vector<double> v2)
{
    vector<double> vt,vans;
    vans.push_back(0);
    for(int i=v2.size();i>0;i--)
    {
        vector<double> v;
        v = coeffexpr(v1,v2[i-1]);
        vt = pushzero(v,v2.size()-i);
        vans = addexpr(vans,vt);
    }
    return vans;
}