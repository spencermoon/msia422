package homework5;

import java.text.*;
import java.util.*; 

/**
 * This is the Monthly subclass.
 * @author Spencer Moon
 */

public class Monthly extends Appointment
{
	private Date start;
	private Date end;
	private int repeatDay;
	
	
	// Define monthly appointment
	public Monthly(String description, int startYear, int startMonth, int endYear, int endMonth, int day) throws ParseException 
	{
		super(description); 
		DateFormat dateFormatter = new SimpleDateFormat(String.format("yyyy-MM-dd")); 
        this.start = dateFormatter.parse(String.format("%d-%d-%d", startYear, startMonth, day)); 
        this.end = dateFormatter.parse(String.format("%d-%d-%d", endYear, endMonth, day)); 
        this.repeatDay = day;
	}
	
	
	// Override superclass occursOn method to check if an appointment occurs on a specified date
	@Override
	public boolean occursOn(int year, int month, int day) throws ParseException 
    { 
        DateFormat dateFormatter = new SimpleDateFormat(String.format("yyyy-MM-dd")); 
        Date checkedDate = dateFormatter.parse(String.format("%d-%d-%d", year, month, day)); 
        return checkedDate.compareTo(start) >= 0 && checkedDate.compareTo(end) <= 0 && day == repeatDay; 
    } 
	
	
	// Allow printing of an appointment
    public String toString() 
    { 
        return String.format("Appointment: %s, Type: Monthly, Start Date: %s, End Date: %s", this.description, this.start.toString(), this.end.toString()); 
    } 
}
