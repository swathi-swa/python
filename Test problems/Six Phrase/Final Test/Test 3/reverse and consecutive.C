#include <stdio.h>
#include<string.h>
int main(void)
{
    char str[30],str1[30];
    int len,ctr,itr;
    scanf("%s",str);
    for(len=0;str[len];len++);
    for(itr=len-1;itr>=0;)
    {
        ctr=itr;
        while(str[ctr]==str[itr])
        {
            itr--;
        }
        printf("%c",str[ctr]);
    }
    return 0;
}


INPUT:

aaaCCCcccccaaaBBBef

OUTPUT:

feBacCa
