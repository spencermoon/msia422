package homework4;

import java.util.Scanner;

/**
 * This is a program that allows users to convert between US dollar and Japanese yen. 
 * The user can select from options 1, 2, and 3 to navigate through the program.
 * @author Spencer Moon
 */

public class exercise1 
{
	public static void main(String[] args) 
	{
		// Set variables
		double rate = 113.56;
		double dollar;
		double yen;
		int option = 0;
		
		Scanner in = new Scanner(System.in);
		
		// Print available options for user
		System.out.println("Welcome to the dollar/yen currency converter.");
		System.out.println("Refer to the following options: ");
		System.out.println("1: Set conversion rate");
		System.out.println("2: Convert dollar or yen");
		System.out.println("3: Quit");
		System.out.println("Default currency rate (as of 11/11/2017) will be used if not set before currency conversion.");
		
		// Create interactive dollar/yen currency converter 
		while (option != 3)
		{
			// Throw out options not in available options
			try
			{
				System.out.print("Choose from the options above: ");
				option = in.nextInt();
				
				if (option == 1)
				{
					System.out.print("Enter price for one dollar in Japanese yen: ");
					rate = in.nextDouble();
				}
				else if (option == 2)
				{
					System.out.print("Which currency would you like to convert [d/y]? ");
				    String convert = in.next();
		
					if (convert.equals("d"))
					{
						System.out.print("Enter dollar amount: ");
						dollar = in.nextDouble();
						yen = dollar * rate;
						System.out.println("Converted yen amount: " + yen);
					}
					else
					{
						System.out.print("Enter yen amount: ");
						yen = in.nextDouble();
						dollar = yen / rate;
						System.out.println("Converted dollar amount: " + dollar);
					}
				}
				else if (option == 3)
				{
					break;
				}
				else
				{
					System.out.println("Please restart the program and choose from the options above.");
					break;
				}
			} 
			catch (Exception e) 
			{
				System.out.println("Please restart the program and choose from the options above.");
				break;
			}
		}
			in.close();
	}

}
