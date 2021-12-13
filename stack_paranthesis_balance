#include<iostream>
#include<string.h>
using namespace std;
#define MAX 50
class balance
{
    public:
char stack[MAX];
int top;
  
balance()
{
      top=-1;
}

void push(char temp) {

  if(top==MAX-1)  {
    cout<<"\n Stack Overflow!!!";
    return;
  }

  top++;
  stack[top]=temp;

}

char pop() {
  if(top==-1)  {
    cout<<"\n Stack Underflow!!!";
    char x='\n';
    return x;
  }
  char temp=stack[top];
  top--;
  return temp;
}
};

int main(){
    char str[MAX];
    int i=0;
    cout<<"\n Enter a String: ";
    cin.getline(str,MAX);
    balance obj;
    if((str[0]==')')||(str[0]==']')||(str[0]=='}'))
    {
        cout<<"Not balanced";
        return 0;
    }
    else
    {
        while(str[i]!='\0')
        {
            char ch=str[i];
            switch(ch)
            {
                case '(':obj.push(ch);break;
                case '[':obj.push(ch);break;
                case '{':obj.push(ch);break;
                case ')':obj.pop();break;
                case ']':obj.pop();break;
                case '}':obj.pop();break;
            }
            i++;
        }
    }
if (obj.top==-1)
{
    cout<<"Balanced";
}
else
{
    cout<<"Not Balanced";
}
return 0;
}
