#include <iostream>
#include <string>
using namespace std;

int main(){
    string input;
    cin >> input;
    double prize= stod(input);
    cout << 100/prize << endl;
    cout << 100/(100-prize)<<endl;
}
