#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    int num,rev;
    scanf("%d",&num);
    int temp;
    temp=num;
    int b=0,s=0;
    while(temp!=0)
    {
        temp=temp/10;
        ++b;
    }
    temp=num;
    while(temp!=0)
    {
        rev=temp%10;
        s+=pow(rev,b);
        temp=temp/10;
    }
    if(s==num)
    {
        printf("Yes");
    }
    else
    {
        printf("No");
    }
    return 0;
}
