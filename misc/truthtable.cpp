#include<iostream>
using namespace std;
void truthtable(bool a,bool b,bool c){
    cout<<endl<<a<<"\t"<<b<<"\t"<<c<<"\t"<<((!a&&b)|(b==c));
}
int main()
{
    bool p=false,q=false,r=false;

    cout<<endl<<"To check 'inclusive or' use || or |"<<endl;
    cout<<"To check 'conditional' relation(p implies q) use !p&&q"<<endl;
    cout<<"To check 'biconditional' relation use p==q"<<endl;
    cout<<"To check 'and' use &&"<<endl;
    cout<<"Use '!' for negation"<<endl;

    cout<<endl<<"p"<<"\t"<<"q"<<"\t"<<"r"<<"\t"<<"!a&&b|b==c"<<endl;

    truthtable(p,q,r);
    p=!p;
    truthtable(p,q,r);
    p=!p;
    q=!q;
    truthtable(p,q,r);
    q=!q;
    r=!r;
    truthtable(p,q,r);
    p=!p;
    q=!q;
    r=!r;
    truthtable(p,q,r);
    r=!r;
    p=!p;
    truthtable(p,q,r);
    p=!p;
    q=!q;
    truthtable(p,q,r);
    q=!q;
    truthtable(p,q,r);
 return 0;
}
