#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    int num;
    scanf("%d", &num);
    int a=0;
    int b=1,c;  
    for(int i=1;i<=num;i++)
    {     
        printf("%d ",a);
        c=a+b;
        a=b;
        b=c;
    }
    
    return 0;
}

