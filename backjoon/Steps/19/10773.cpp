#include <iostream>
#include <string>
#define SIZE 100000
using namespace std;

struct  stack{
    int top=-1;
    int arr[SIZE];
};
void push(struct stack *S, int n){
    if(S->top==SIZE-1){

    }else {
        int top;
        S->top +=1;
        top = S->top;
        S->arr[top] = n;
    }
}

int pop(struct stack *S){
    if(S->top==-1){
        return 0;
    }else {
        int temp;
        int top = S->top;
        temp = S->arr[top];
        S->top = S->top -1;
        return temp;
    }
}
int empty(struct stack *S){
    if(S->top == -1) return 1;
    else return 0;
}
int main()
{
    ios_base::sync_with_stdio(false);
    struct stack S;
    int input=0,num=0;
    int i,del=0,all=0;
    cin>>num;
    
    for(i=0;i<num;i++){
        cin>>input;
        
        if(input!=0){
            push(&S,input);
            all+=input;
        }else if(input==0){
           del+= pop(&S);
        }
    }
    cout<<all-del<<endl;
    return 0;
}
