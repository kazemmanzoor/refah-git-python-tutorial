
#include <stdio.h>

int
main (void)
{

// your code goes here

  float a, b, c, d;

  scanf ("%f", &a);

  printf ("real of num1= %f\n", a);
  scanf ("%f", &b);

  printf ("real of num2= %f\n", b);

  scanf ("%f", &c);

  printf ("img of num1 = %f\n", c);
  scanf ("%f", &d);

  printf ("img of num2= %f\n", d);

  printf ("sum= %f + %f i\n", (a + b), (c + d));
  printf ("mul= %f + %f i", ((a * c) - (b * d)), ((a * d) + (b * c)));
}
