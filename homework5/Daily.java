package homework5;

import java.text.*;
import java.util.*; 

/**
 * This is the Daily subclass.
 * @author Spencer Moon
 */

public class Daily extends Appointment
{
	public Date start;
	public Date end;
	
	
	// Define daily appointment
	public Daily(String description, int startYear, int startMonth, int startDay, int endYear, int endMonth, int endDay) throws ParseException 
	{
		super(description); 
		DateFormat dateFormatter = new SimpleDateFormat(String.format("yyyy-MM-dd")); 
        this.start = dateFormatter.parse(String.format("%d-%d-%d", startYear, startMonth, startDay)); 
        this.end = dateFormatter.parse(String.format("%d-%d-%d", endYear, endMonth, endDay)); 
	}
	
	
	// Override superclass occursOn method to check if an appointment occurs on a specified date
	@Override
	public boolean occursOn(int year, int month, int day) throws ParseException 
    { 
        DateFormat dateFormatter = new SimpleDateFormat(String.format("yyyy-MM-dd")); 
        Date checkedDate = dateFormatter.parse(String.format("%d-%d-%d", year, month, day)); 
        return checkedDate.compareTo(start) >= 0 && checkedDate.compareTo(end) <= 0;
    } 
	
	
	// Allow printing of an appointment
	public String toString() 
    { 
        return String.format("Appointment: %s, Type: Daily, Start Date: %s, End Date: %s", this.description, this.start.toString(), this.end.toString()); 
    } 
}
