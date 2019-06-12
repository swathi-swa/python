
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    long a;
    int re;
    long sum=0;
    scanf("%ld",&a);
    while(a>0)
    {
        re=a%10;
        sum=sum*10+re;
        a=a/10;
    }
    
    printf("%ld",sum);
    return 0;
}

