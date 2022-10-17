sum:
public static void Main (string[] args)
        {
            Complex C1 = new Complex(3, 2);
            C1.printComplexNumber();
            Complex C2 = new Complex(9, 5);
            C2.printComplexNumber();
            Complex C3 = new Complex();
            C3 = C3.addComp(C1, C2);
            Console.WriteLine("Sum of ");
            C3.printComplexNumber();
            Console.WriteLine ("Press any key to Finish Program");
            Console.ReadKey ();
        }
        
        public class Complex {
        int real, imaginary;
        public Complex() {
        }
        public Complex(int real, int imaginary) {
            this.real = real;
            this.imaginary = imaginary;
        }
        public Complex addComp(Complex C1, Complex C2) {
            Complex temp = new Complex();
            temp.real = C1.real + C2.real;
            temp.imaginary = C1.imaginary + C2.imaginary;
            // returning the sum
            return temp;
        }
        public void printComplexNumber() {
            Console.WriteLine("Complex number: " + real + " + " + imaginary + "i");
        }
    }
    
    
    
    
    sub:
    public static void Main (string[] args)
        {
            // First Complex number 
            Complex C1 = new Complex(3, 2); 
            // printing first complex number 
            C1.printComplexNumber(); 
            // Second Complex number 
            Complex C2 = new Complex(9, 5); 
            // printing second complex number 
            C2.printComplexNumber(); 
            Complex C3 = new Complex(); 
            C3 = C3.subtract(C1, C2); 
            Console.WriteLine("Difference of "); 
            C3.printComplexNumber(); 
            Console.WriteLine ("Press any key to Finish Program !!");
            Console.ReadKey ();
        }
        
        public class Complex {
        int real, imaginary;
        public Complex() {
        }
        public Complex(int real, int imaginary) {
            this.real = real;
            this.imaginary = imaginary;
        }
            
        public Complex subtract(Complex C1, Complex C2) {
            Complex temp = new Complex();
            temp.real = C1.real - C2.real;
            temp.imaginary = C1.imaginary - C2.imaginary;
            return temp;
        }
            
        public void printComplexNumber() {
            Console.WriteLine ("Complex number: " + real + " + " + imaginary + "i");
        }
    }
    
    
    
    
    
    
    
   mul:
     public static void Main (string[] args)
        {
            Complex C1 = new Complex(3, 2);
            C1.printComplexNumber();
            Complex C2 = new Complex(9, 5);
            C2.printComplexNumber();
            Complex C3 = new Complex();
            C3 = C3.Multiplication(C1, C2);
            Console.WriteLine("Multiplication of ");
            C3.printComplexNumber();
            Console.WriteLine ("Press any key to finish Program...");
            Console.ReadKey ();
        }
        
       public class Complex {
        int real, imaginary;
        public Complex() {
        }
        public Complex(int real, int imaginary) {
            this.real = real;
            this.imaginary = imaginary;
        }
        public Complex Multiplication(Complex C1, Complex C2) {
            Complex temp = new Complex();
            temp.real = C1.real * C2.real - C1.imaginary * C2.imaginary;
            temp.imaginary = C1.real * C2.imaginary + C1.imaginary * C2.real;
            return temp;
        }
        public void printComplexNumber() {
            Console.WriteLine("Complex number: " + real + " + " + imaginary + "i");
        }
    } 
