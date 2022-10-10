
#include<stdio.h>

struct complex
{
    float real;
    float i;
};

int main()
{
   
    struct complex a, b, mult;
    printf("Enter real and imaginary part of first complex number:\n");
    scanf("%f%f", &a.real, &a.i);
    printf("Enter real and imaginary part of second complex number:\n");
    scanf("%f%f", &b.real, &b.i);

    mult.real = a.real * b.real - a.i * b.i;
    mult.i = a.real * b.i + b.real * a.i;

    printf("PRODUCT = %0.3f +  %0.3f i", mult.real, mult.i);

    return 0;
}
