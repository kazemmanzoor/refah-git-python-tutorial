// C++ program 

using namespace std;

void print_product(int a, int b,

                   int c, int d)
{
    int prod1 = a * c;
    int prod2 = b * d;
    int prod3 = (a + b) * (c + d);
    int real = prod1 - prod2;

    int imag = prod3 - (prod1 + prod2);
    

    cout << real << " + " << imag << "i";
}
 


int main()
{

    int a, b, c, d;
    // Given four Numbers

    a = 2;

    b = 3;

    c = 4;

    d = 5;

    print_product(a, b, c, d);

    return 0;
}