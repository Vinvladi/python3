#include <stdio.h>

int main() {
   int a,b,c;
    scanf("%d", &a);
   b = 1;
   c = 1;
   while (a>=b)
   {   c = b*c;
       b = b+1;
   }
    printf("%d", c);
   return 0;
}
