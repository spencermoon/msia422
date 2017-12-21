package homework4;

/**
 * This is a program that extracts data from a text file and prints some information about the data.
 * It also creates a text file output with employees sorted by their salaries.
 * @author Spencer Moon
 */

import java.io.*;
import java.util.*;
import java.text.ParseException;

public class exercise3 
{
	public static void main(String[] args) throws IOException, ParseException
	{
		// Extract data from text file
		String path = "employees.txt";
		File file = new File(path);
		List<String> name = new ArrayList<>();
		List<String> dob = new ArrayList<>();
		List<String> salary = new ArrayList<>();
		List<String> output = new ArrayList<>();
		
		try (BufferedReader bufferedReader = new BufferedReader(new FileReader(file))) 
		{
			String line; 
			while ((line = bufferedReader.readLine()) != null) 
			{
				name.add(line.split(",")[0]);
				dob.add(line.split(",")[1]);
				salary.add(line.split(",")[2]);
			}
		}
		
		// Initialize variables
		double tot_sal = 0;
		double tot_age = 0;
		int above_avg = 0;
		String max = salary.get(0);
		String maxname = "";
		String header = "SALARY, NAME";
		
		// Calculate total employee salary
		for (String s : salary)
		{
			tot_sal = tot_sal + Double.parseDouble(s);
		}
		
		// Count the number of employees with above average salary
		for (String s : salary)
		{
			if (Double.parseDouble(s) > tot_sal/salary.size())
			{
				above_avg++;
			};
		}
		
		// Calculate total employee age
		for (String d : dob)
		{
			double age = 2017 - Double.parseDouble(d.substring(6));
			tot_age = tot_age + age;
		}
		
		// Calculate maximum salary
		for (int i = 0; i < salary.size(); i++) {
		    if (Double.parseDouble(salary.get(i)) > Double.parseDouble(max)) 
		    {
		      max = salary.get(i);
		    }
		}
		
		// Grab employee with the highest salary
		for (int i = 0; i < name.size(); i++)
		{
			if (salary.get(i) == max)
			{
				maxname = name.get(i);
			}
		}
		
		// Print calculations
		System.out.println("Number of employees: " + name.size());	
		System.out.println("Employee with highest salary: " + maxname);
		System.out.println("Average salary: " + Math.round(tot_sal/salary.size()*100)/100);
		System.out.println("Number of employees with salaries above average: " + above_avg);
		System.out.println("Average age: " + Math.round(tot_age/dob.size()));
		
		// Sort employees based on salary
		for (int i = 0; i < name.size(); i++)
		{
			output.add(salary.get(i) + "," + name.get(i));
			//System.out.println(output.get(i));
		}
		Collections.sort(output);
		
		// Export file
		BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(path.replace("txt", "csv")));
		bufferedWriter.write(header+"\n");
		for (String o : output) {
			bufferedWriter.write(o+"\n");
		}
		bufferedWriter.close();
	}
	
}
