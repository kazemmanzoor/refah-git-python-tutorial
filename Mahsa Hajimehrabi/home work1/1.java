public class Complex {
 int real, imaginary;
 public static void main (String[] args) {
 Complex C1 = new Complex(4, 2);
 C1.printComplexNumber();
 Complex C2 = new Complex(3, 5);
 C2.printComplexNumber();
 Complex C3 = new Complex();
 C3 = C3.addComp(C1, C2);
 System.out.print("Sum of ");
 C3.printComplexNumber();
}
 public Complex() {
 }
 public Complex (int real, int imaginary) {
 this.real = real;
 this.imaginary = imaginary;
 }
 Complex addComp (Complex C1, Complex C2) {
 Complex temp = new Complex();
 temp.real = C1.real + C2.real;
 temp.imaginary = C1.imaginary + C2.imaginary;
 // returning the sum
 return temp;
 }
 void printComplexNumber() {
 System.out.println ("Complex number: " + real + " + " + imaginary + "i");

}
}


















