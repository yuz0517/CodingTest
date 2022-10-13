#include <iostream>
#include <string>
using namespace std;
int main(){
  	//문자열 덧셈으로 해결
    string id="";
    
    getline(cin,id);
    id += "??!"; // id = id+"??!";
    cout<<id<<endl;
    return 0;
}
    
