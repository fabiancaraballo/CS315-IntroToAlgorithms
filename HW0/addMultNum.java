import java.util.Scanner;     //import Scanner package
import java.io.File;
import java.util.Arrays;

public class addMultNum {
	public static void main(String[] args){
	
		// Create a Scanner that reads system input
		Scanner scanner = new Scanner(System.in);

		String lineChecker = scanner.nextLine();
		int numLines = Integer.parseInt(lineChecker);
		
		// Loop over the scanner's input
		for(int i = 0; i < numLines; i++) {
			String fileLine = scanner.nextLine();
			//System.out.println(fileLine);

			String[] arr = fileLine.split(" ");
			//System.out.println(arr);

			int x = Integer.parseInt(arr[0]);
			int y = Integer.parseInt(arr[1]);
	
			int addNum = x + y;
			int multNum = x * y;

			System.out.println(addNum + " " + multNum);
			//System.out.println(addNum); 
			//System.out.println(multNum);

		}
		



		// Close the Scanner		
		scanner.close();
	}
	
}

