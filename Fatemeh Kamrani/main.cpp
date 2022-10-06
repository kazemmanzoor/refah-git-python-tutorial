#include<bits/stdc++.h>
using namespace std;

typedef struct Complex
{
  float real;
  float imag;
  void display ();

} Complex;

void
Complex::display ()
{
  cout << real << "+" << imag << "i" << endl;
}

Complex Multiply (Complex, Complex);

int
main ()
{
  Complex z1, z2, ans_mul, ans_add;

  cout << "Enter the real and imaginary parts of the first complex number:";
  cin >> z1.real >> z1.imag;
  cout << "z1 = ";
  z1.display ();
  //z1=a+bi

  cout << "Enter the real and imaginary parts of the second complex number:";
  cin >> z2.real >> z2.imag;
  cout << "z2 = ";
  z2.display ();
  //z2=c+di

  //ans_mul=(ac-bd)+i(ad+bc)
  ans_mul.real = (z1.real * z2.real) - (z1.imag * z2.imag);
  ans_mul.imag = (z1.real * z2.imag) + (z1.imag * z2.real);
  cout << "The result after the multiplication of z1 and z2 is: " << endl;
  cout << "z1.z2 = ";
  ans_mul.display ();

//ans_add=(a+c)+i(b+d)
  ans_add.real = (z1.real + z2.real);
  ans_add.imag = (z1.imag + z2.imag);
  cout << "The result after the Addition of z1 and z2 is: " << endl;
  cout << "z1+z2 = ";
  ans_add.display ();

  return 0;
}
