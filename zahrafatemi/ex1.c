// c program mul
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



// c program sum
#include <stdio.h>
 
struct complex
{
   int real, imaginary;
};
 
main()
{
    struct numbers a, b, c ;
 
    printf("Enter value of a and b complex number a + ib.\n");
    printf("value of complex number a is = ");
    scanf("%d", &a.real);
    printf("value of complex number b is = ");
    scanf("%d", &a.imaginary);
    printf("Enter value of c and d complex number c + id.\n");
    printf("value of complex number c is = ");
    scanf("%d", &b.real);
    printf("value of complex number d is = ");
    scanf("%d", &b.imaginary);
    c.real = a.real + b.real;
    c.imaginary = a.imaginary + b.imaginary;
    if (c.imaginary >= 0)
        printf("complex numbers sum is = %d + %di\n", c.real, c.imaginary);
    else
        printf("complex numbers sum = %d %di\n", c.real, c.imaginary);
    return 0;
}
