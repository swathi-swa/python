#include<stdio.h>
int main()
{
  int n;
  int s=0;
  scanf("%d",&n);
  for(int i=0;i<n;i++)
  {
    if(n%i==0)
    {
      s=s+i
    }
  }
  if(s==n)
  {
    printf("%s","YES");
  }
  else
  {
    printf("%S","NO");
  }
  return 0;
}
