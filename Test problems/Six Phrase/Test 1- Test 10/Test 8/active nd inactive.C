#include <stdio.h>

int main() {
	int a[8],na[8],i;
	for(i=0;i<8;i++)
	    scanf("%d ",&a[i]);
	na[0]=a[1];
    na[7]=a[6];
	for(i=1;i<7;i++)
	    na[i]=a[i-1]^a[i+1];
	for(i=0;i<8;i++)
    	printf("%d ",na[i]);
	return 0;
}


INPUT:
1 0 0 0 0 1 0 0 

OUTPUT:

0 1 0 0 1 0 1 0
