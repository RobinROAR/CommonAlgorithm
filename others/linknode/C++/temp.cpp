#include<iostream>
using namespace std;

int main(){
cout<<"nice"<<endl;
int* p = new int[20];
cout<<p<<endl;
delete [] p;
cout<<p<<endl;
p = NULL;
delete p;



return 0;

}

