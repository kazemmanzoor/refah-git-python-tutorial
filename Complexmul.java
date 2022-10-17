
package complexmul;


public class Complexmul {
int real,imaginary;
public Complexmul(){
    
}
 public Complexmul(int real,int imaginary){
     this.real=real;
     this.imaginary=imaginary;
 }  
 Complexmul Multiplication(Complexmul C1,Complexmul C2){
     Complexmul temp=new Complexmul();
     temp.real=C1.real*C2.real-C1.imaginary*C2.imaginary;
    temp.imaginary=C1.real*C2.imaginary+C1.imaginary*C2.real;
    return temp;
     
 }
 void printComplexNumber(){
    System.out.println("Complex number :" +real+ "+" +imaginary+ "i");
}
    public static void main(String[] args) {
        // TODO code application logic here
    }
    
}
