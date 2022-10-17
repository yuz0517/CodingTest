//시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력
#include <iostream>
using namespace std;

int main(){
    int input;
    cin>>input;
    if(input>=90&&input<=100) cout<<"A"<<endl;
    else if(input>=80&&input<=89) cout<<"B"<<endl;
    else if(input>=70&&input<=79) cout<<"C"<<endl;
    else if(input>=60&&input<=69) cout<<"D"<<endl;
    else cout<<"F"<<endl;
    return 0;
}
