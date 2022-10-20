//결과를 저장: string변수 사용
//간
#include <iostream>
#include <string>
#include <cstring>
#define SIZE 50
using namespace std;
struct  stack{
    int top=-1;
    char arr[SIZE];
};
void push(struct stack *S, char n){
    if(S->top==SIZE-1){

    }else {
        int top;
        S->top +=1;
        top = S->top;
        S->arr[top] = n;
    }
    
}

char pop(struct stack *S){
    if(S->top==-1){
        return 0;
    }else {
        char temp;
        char top = S->top;
        temp = S->arr[top];
        S->top = S->top -1;
        return temp;
    }
}
int isempty(struct stack *S){
    
    if(S->top == -1) return 1;
    else return 0;
}
int main(){
   string input;
   
    int n=0,length=0;
    cin>>n;
    while(n>0){
        n--;
    
       stack S={};
       string result="YES";
       cin>>input;
       length = input.length();
     
        for(int j=0;j<length;j++){
            if(input[j]=='('){
                push(&S,input[j]);
            }else if(input[j]==')'){
    
                if(isempty(&S)){
                  //비어있는상태에서 )가 나오면 그 순간부터 vps가 아니게 됨
                   result="NO";
                   break; 
                }else pop(&S);
            }else continue;
        }
        
        if(isempty(&S)==0){
            result="NO";
        }   
        cout<<result<<endl;
        
    }
    
    return 0;
    
}
