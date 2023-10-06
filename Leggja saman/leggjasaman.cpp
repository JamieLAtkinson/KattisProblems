#include <iostream>
#include <string>
using namespace std;

int main(){
    string n1;
    string n2;
    getline(cin,n1);
    getline(cin,n2);
    
    cout << stoi(n1)+stoi(n2);
    return 0;
}
