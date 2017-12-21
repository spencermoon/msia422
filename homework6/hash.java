//Homework 6
//Spencer Moon & Anisha Dubhashi

package homework6;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.lang.reflect.Array;
import java.util.*;

public class hash {

	//1. create ASCII hash arraylist
	public static ArrayList<Integer> create_hash_ascii(ArrayList<String> names, int n) {
		ArrayList<Integer> hash_ascii = new ArrayList<Integer>(); 
		for (String s : names) { 
			int sum_c = 0;
			for(char c : s.toCharArray()) {
				sum_c += (int) c; 
			}
			hash_ascii.add(sum_c % n); 
		}
		return hash_ascii; 
	}
	
	//2. create Java hash arraylist
	public static ArrayList<Integer> create_hash_jvm(ArrayList<String> names, int n) {
		ArrayList<Integer> hash_jvm = new ArrayList<Integer>(); 
		for (int k = 0; k < names.size(); k++) {
			hash_jvm.add(java.lang.Math.abs(names.get(k).hashCode() % n)); 
			}
		return hash_jvm; 
	}
	
	//3. create new hash arraylist
	public static ArrayList<Integer> create_hash_new(ArrayList<String> names, int n) {
		ArrayList<Integer> hash_new = new ArrayList<Integer>(); 
		int m = 0; 
		for (String s : names) { 
			hash_new.add(m % n); 
			m++;
		}
		return hash_new; 
	}
	
	//create output
	public static String[] create_hash_map(ArrayList<String> names, int n, ArrayList<Integer> hash_array) {
		//create map with key value pairs + collision
		Map<Integer, ArrayList<String>> hm = new HashMap<Integer, ArrayList<String>>();
		int k = 0;
		for (Integer h : hash_array) {
			//if there is no hash value, add an array list
			if(!hm.containsKey(h)) {
		        hm.put(h, new ArrayList<String>());
		    	}
			//next, add the name to the array list
		    hm.get(h).add(names.get(k));
		    k++;
		}
		//create output array
		String output[] = new String[n];
		for (int key : hm.keySet()) {
			output[key] = hm.get(key).toString().replace("[", "").replace("]","").trim();
			}
		return output;
	}

	//export text file
	public static void export_hash(int n, String[] output, String file_name) throws IOException {
		//export text file and calculate load factor
		//load factor is defined as proportion of values that are full
		//higher load factor indicates that values are more spread out in the hashes
		double counter = 0;
		FileWriter writer = new FileWriter(file_name); //"output2.txt"
		for (int i = 0; i < Array.getLength(output); i++) {
			if (output[i] == null) {
				writer.write(i + " EMPTY LINE...");
				writer.write("\n\n");
				counter = counter + 1;
				}
			else {
				writer.write(i + " " + output[i]);
				writer.write("\n\n");
				}		  
			}
		writer.write("\n");	
		writer.write("Load Factor: " + (1 - counter/n));
		//System.out.print("Load Factor: " + (1 - counter/n) + "\n");
		writer.close();
	}
	
	//main
	public static void main(String[] args) throws IOException {
		Scanner in = new Scanner(System.in);
		System.out.print("Specify size of array (100, 200, or any integer > 0): ");
		
		int n = 100;
		
		//try and catch to make sure user enters appropriate number
		boolean done = false; 
		while (!done) { 
			try {
				n = in.nextInt();
				
				//if user enters number < 1, throw exception
				if (n < 1) {
					throw new IllegalArgumentException();
					}
				//continue if user enters number > 1
				done = true;
				}
			catch (IllegalArgumentException e)
			{
				System.out.println("You entered an invalid entry. Please enter an integer > 0:");
			}
			catch (InputMismatchException e)
			{
				System.out.println("You entered an invalid entry. Please enter an integer > 0:");
				in.next(); // this consumes the invalid token
			}
		}
		
		in.close();
		
		String pathname = "./input.txt";
		File file = new File(pathname);
		
		//create names arraylist
		ArrayList<String> names = new ArrayList<>();
		try (BufferedReader bufferedReader = new BufferedReader(new FileReader(file))) {
			String line; 
			while ((line = bufferedReader.readLine()) != null) {
				names.add(line);
				}
			}		
		export_hash(n, create_hash_map(names, n, create_hash_ascii(names, n)), "output1.txt");
		export_hash(n, create_hash_map(names, n, create_hash_jvm(names, n)), "output2.txt");
		export_hash(n, create_hash_map(names, n, create_hash_new(names, n)), "output3.txt");	
		System.out.print("Output files created. Load factor is included at bottom of output file. ");
	}
}
