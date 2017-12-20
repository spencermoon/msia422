package homework5;

import java.text.*;
import java.util.*; 
import java.io.*;

/**
 * This is the appointment management program.
 * It allows users to add appointments, export added appointments, and verify which appointments are on a specific date.
 * @author Spencer Moon
 */

public class Manager 
{
    	static int quit = 0;
    	static ArrayList<String> output = new ArrayList<String>();
    	static ArrayList<Appointment> appointment = new ArrayList<Appointment>();
    	
    	
    	// Add method allows users to input appointment details and add an one-time, daily, or monthly appointment
    	public static void Add() throws ParseException
    	{
    		Scanner in = new Scanner(System.in);
    		int apptType;
    		int startYear;
    		int startMonth;
    		int endYear;
    		int endMonth;
    		int day;
    		int startDay;
    		int endDay;
    		String description;
    		
    		System.out.print("\nWhat type of appointment would you like to add?\nEnter 1 for one-time, 2 for daily, and 3 for monthly: ");
		apptType = in.nextInt();
		
		// Add an one-time appointment
		if (apptType == 1)
		{
			System.out.print("Enter appointment year: ");
			startYear = in.nextInt();
			System.out.print("Enter appointment month: ");
			startMonth = in.nextInt();
			System.out.print("Enter appointment day: ");
			startDay = in.nextInt();
			System.out.print("Enter appointment description: ");
			description = in.next();
			Appointment o = new Onetime(description, startYear, startMonth, startDay);
			output.add(o.toString());
			appointment.add(o);
			System.out.println("\nAppointment has been added.\n");
		}
		// Add a daily appointment
		else if (apptType == 2)
		{
			System.out.print("Enter appointment start year: ");
			startYear = in.nextInt();
			System.out.print("Enter appointment start month: ");
			startMonth = in.nextInt();
			System.out.print("Enter appointment start day: ");
			startDay = in.nextInt();
			System.out.print("Enter appointment end year: ");
			endYear = in.nextInt();
			System.out.print("Enter appointment end month: ");
			endMonth = in.nextInt();
			System.out.print("Enter appointment end day: ");
			endDay = in.nextInt();
			System.out.print("Enter appointment description: ");
			description = in.next();
			Appointment d = new Daily(description, startYear, startMonth, startDay, endYear, endMonth, endDay);
			output.add(d.toString());
			appointment.add(d);
			System.out.println("\nAppointment has been added.\n");
		}
		// Add a monthly appointment
		else if (apptType == 3)
		{
			System.out.print("Enter appointment start year: ");
			startYear = in.nextInt();
			System.out.print("Enter appointment start month: ");
			startMonth = in.nextInt();
			System.out.print("Enter appointment end year: ");
			endYear = in.nextInt();
			System.out.print("Enter appointment end month: ");
			endMonth = in.nextInt();
			System.out.print("Enter appointment recurring day: ");
			day = in.nextInt();
			System.out.print("Enter appointment description: ");
			description = in.next();
			Appointment m = new Monthly(description, startYear, startMonth, endYear, endMonth, day);
			output.add(m.toString());
			appointment.add(m);	
			System.out.println("\nAppointment has been added.\n");
		}
		
    	}
    	
    	
    	// Menu allows users to select what action needs to be taken within the appointment manager
	public static void Menu() throws IOException, ParseException
    {
		int option;
		Scanner in = new Scanner(System.in);
		int startYear;
		int startMonth;
		int startDay;
		
    		System.out.println("Welcome to the appointment manager.");
    		System.out.println("Refer the following options:");
    		System.out.println("1: Add appointment");
    		System.out.println("2: Export all appointments");
    		System.out.println("3: Print appointments on specified date");
    		System.out.println("Press any other number to quit.");
    		System.out.print("\nChoose from the options above: ");
    		
		option = in.nextInt();
		
		// Add an appointment
		if (option == 1)
		{
			Add();
		}
		// Export all appointments
		else if (option == 2)
		{
			FileWriter writer = new FileWriter("appointment.txt"); 
			for(String str: output) {
			  writer.write(str);
			  writer.write("\n");
			}
			writer.close();
			System.out.println("\nAll appointments have been exported.\n");
			
		}
		// Print appointments occurring on a specified date
		else if (option == 3)
		{
			System.out.print("Enter appointment year: ");
			startYear = in.nextInt();
			System.out.print("Enter appointment month: ");
			startMonth = in.nextInt();
			System.out.print("Enter appointment day: ");
			startDay = in.nextInt();
			System.out.print("\n");
			for (Appointment a : appointment)
			{
				if (a.occursOn(startYear, startMonth, startDay))
				{
					System.out.println(a.toString());
				}
			}
			System.out.print("\n");
		}
		// Quit the program
		else
		{
			quit = 1;
		}
    			
    }
	
	
	// Run all methods within the class
	public static void main(String[] args) throws ParseException, IOException
    {
    		try
    		{
			while (quit == 0)
	    		{
	    			Menu();
	    		}
    		}
    		catch (Exception e)
    		{
    			System.out.print("Please restart the program and enter an appropriate input.");
    		}
    }
}
