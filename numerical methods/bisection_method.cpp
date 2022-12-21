#include<bits/stdc++.h>
using namespace std;
double func(double x){
    //replace your desired function here
    return x*x*x+4*x*x-10;
   //return sqrt(x)-cos(x);
}
int main()
{
    double lower,upper,eps,p;

    //Find a interval as small as possible 

    cout<<"Enter the lower and upper bound respectively:"<<endl;
    cin>>lower>>upper;
    cout<<"Enter the precision range:"<<endl;
    cin>>eps;

    if(func(lower)*func(upper)<0){
    while(upper-lower>=eps){
        p=(lower+upper)/2;
        if(func(p)==0)
        break;
        if(func(p)<0)
        lower=p;
        else
        upper=p;
    }
    }
    if(func(lower)*func(upper)>0)
    cout<<"Enter a valid interval using IVP"<<endl;
    
    cout<<setprecision(5)<<"The approximate root is : "<<p<<endl;
   
   
 return 0;
}