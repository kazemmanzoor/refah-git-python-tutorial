
public class OP_Complex_Number {

	public static void main(String[] args) {
		Complex C1 = new Complex(4, 3);
		C1.printComplexNumber();

		Complex C2 = new Complex(8, 2);

		C2.printComplexNumber();

		Complex C3 = new Complex();

		C3 = C3.addComp(C1, C2);

		System.out.print("Sum of ");
		C3.printComplexNumber();

   
    Complex C4 = new Complex();

		C4 = C4.subtract(C1, C2);

		System.out.print("Sub of ");
		C4.printComplexNumber();
	}

}
