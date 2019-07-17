#include<stdio.h>
#include,conio.h>
int main()
{
  double a,b,c;
  scanf("%lf %lf %lf",&a,&b,&c);
  double s=0,k=0;
  s=(a+b+c)/2;
  k=sqrt(s*(s-a)*(s-b)*(s-c));
  printf("%.2lf",k);
  return 0;
}
