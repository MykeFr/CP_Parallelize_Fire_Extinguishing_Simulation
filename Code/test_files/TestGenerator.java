import java.util.Scanner;
import java.io.File;
import java.io.IOException;
import java.io.FileWriter;
import java.lang.Math;



public class TestGenerator{


	//private int size1, size2, maxIter, numTeams, numFocalPoints;


	public static void main(String[] args){
		Scanner in = new Scanner(System.in);

		System.out.print("Size 1 = ");
		int size1 = in.nextInt();

		System.out.print("Size 2 = ");
		int size2 = in.nextInt();

		System.out.print("MaxIter = ");
		int maxIter = in.nextInt();

		System.out.print("NumTeams = ");
		int numTeams = in.nextInt();

		System.out.print("num FocalPoints = ");
		int numFocalPoints = in.nextInt();


		try {
      		File myObj = new File("Test");
      		if (myObj.createNewFile()) {
        	System.out.println("File created: " + myObj.getName());
      	} else {
        	System.out.println("File already exists.");
      	}
    	} catch (IOException e) {
      		System.out.println("An error occurred.");
      		e.printStackTrace();
    	}

    	try {
      		FileWriter myWriter = new FileWriter("Test");

      		//First line
      		String line1 = Integer.toString(size1) + " " + Integer.toString(size2) + " " + Integer.toString(maxIter) + "\n";
      		myWriter.write(line1);


      		//Teams
      		myWriter.write(Integer.toString(numTeams) + "\n");
      		for (int i = 0; i < numTeams; i++){
      			int x = (int) (Math.round(Math.random() * size1));
      			int y = (int) (Math.round(Math.random() * size2));
      			int capacity = (int) (Math.round(Math.random() * 2 + 1));
      			String team =Integer.toString(x) + " " + Integer.toString(y) + " " + Integer.toString(capacity) + "\n";
      			myWriter.write(team);
      		}
      		

      		//Focal Points
      		myWriter.write(Integer.toString(numFocalPoints) + "\n");
      		for(int j = 0; j < numFocalPoints; j++){
      			int x = (int) (Math.round(Math.random() * size1));
      			int y = (int) (Math.round(Math.random() * size2));
      			int step = (int) (Math.round(Math.random() * maxIter));
      			int heat = (int) (Math.round(Math.random() * 1100 + 100));
      			String focal = Integer.toString(x) + " " + Integer.toString(y) + " " + Integer.toString(step) + " " +  Integer.toString(heat) + "\n";
      			myWriter.write(focal);
      		}

      		myWriter.close();
      		System.out.println("Successfully wrote to the file.");
    	} catch (IOException e) {
      		System.out.println("An error occurred.");
      		e.printStackTrace();
    	}

	}

}