#include <iostream>
#include <string>
#define SIZE 10000
#define INPUT 10000
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
        return -1;
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

int top(struct stack *S){
    int re;
    if (empty(S)==1){
        re=-1;
    }
    else if(empty(S)==0){
        int temp;
        int top=S->top;
        temp = S->arr[top];
        re= temp;
    }
    return re;
    
}

int size(struct stack *S){
    
    if (empty(S)==1){return 0;}
    else return S->top+1;
}
int main()
{
    ios_base::sync_with_stdio(false);
    struct stack S;
    string input;
    //char ch_input[INPUT];
    int int_input;
    int i,n;
    cin>>int_input;
    //cin.ignore();
    for(i=0;i<int_input;i++){
        //getline(cin,input);
        cin>>input;
        //cin.ignore();
        if(input == "push"){
            cin >> n;
            
            push(&S,n);
            //cin.ignore();
        }
        else if(input.compare("top") == 0){
            cout<<top(&S)<<endl;
        }else if(input.compare("pop")==0){
            cout<<pop(&S)<<endl;
        }else if(input.compare("size")==0){
            cout<<size(&S)<<endl;
        }else if(input.compare("empty")==0){
            cout<<empty(&S)<<endl;
        }
    }
    

    return 0;
}
