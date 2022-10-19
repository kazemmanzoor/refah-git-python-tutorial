
package complex;


public class Complex {
int real,imaginary;
public Complex(){
}
  public Complex(int real,int imaginary){
      this.real=real;
      this.imaginary=imaginary;
  }
Complex addComp(Complex C1,Complex C2){
    Complex temp=new Complex();
    temp.real=C1.real+C2.real;
    temp.imaginary=C1.imaginary+C2.imaginary;
    //return the sum of complex numbers
    return temp;
   
}
   void printComplexNumber(){
    System.out.println("Complex number :" +real+ "+" +imaginary+"i");
}
   
    public static void main(String[] args) {
      
    
    }
    
}
