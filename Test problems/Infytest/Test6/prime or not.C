#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    int num;
    scanf("%d",&num);
    int flag=0;
    for(int i=2;i<=num/2;i++)
    {
        if(num%i==0)
        {
            flag=1;
            printf("No");
            break;
        }
    }
    if(flag==0)
    {
        printf("Yes");
    }
    return 0;
}
