#include <stdio.h>

int main() {
    int a, b;
    float c,d;
	scanf("%d %d %f", &a, &b);
    c = a%b;
    d = b%a;
    if (c>d)
    {
       printf ("%.0lf",d);
    }
    else
    {
        printf ("%.0lf",c);
    }
            return 0;
}