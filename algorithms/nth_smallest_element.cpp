//nth smallest element of an array using quicksort
#include<iostream>
#include<bits/stdc++.h>
using namespace std;
void quicksort(int arr[],int start,int end ){
    int pivot=arr[start];
    int i=start;int j=end;
    if(start<end){
    while(i<j){
    while(arr[i]<=pivot){
        i++;
    }
    while(arr[j]>pivot){
        j--; 
    }
    if(i<j){
    swap(arr[i],arr[j]);}
    }
    swap(arr[start],arr[j]);
   quicksort(arr,start,j-1);
   quicksort(arr,j+1,end);
    }
}

int main()
{
    int n,k,p;
    cout<<"Enter the array size: ";
    cin>>n;
    int arr[n];
    for(k=0;k<n;k++){
        cin>>arr[k];
    }
    quicksort(arr,0,n-1);
   cout<< "Enter the nth element you want to know: ";
   cin>>p;
   cout<<arr[p-1];

   
 return 0;
}