
#include<iostream>
using namespace std;
int main()
{
    int n,d,m,k,count=0;
    int arr[n];
    cin>>n;

    //enter the array

    for(k=0;k<n;k++){
        
        cin>>arr[k];
    }
    cin>>d>>m;

    // prefix sum array

    for(k=1;k<n;k++)

    arr[k]=arr[k]+arr[k-1];

    if(arr[m-1]==d)

    count++;

    for(k=m;k<n;k=k+1){

        if((arr[k]-arr[k-m])==d)

        count++;
    }

    cout<<count<<endl;

 return 0;
}