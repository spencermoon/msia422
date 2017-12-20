package homework5;

import java.text.*;
import java.util.*; 

/**
 * This is the Onetime subclass.
 * @author Spencer Moon
 */

public class Onetime extends Appointment
{
	private Date date;
	
	
	// Define one-time appointment
	public Onetime(String description, int year, int month, int day) throws ParseException 
	{ 
        super(description); 
        DateFormat dateFormatter = new SimpleDateFormat(String.format("yyyy-MM-dd")); 
        this.date = dateFormatter.parse(String.format("%d-%d-%d", year, month, day)); 
    } 
	
	
	// Override superclass occursOn method to check if an appointment occurs on a specified date
	@Override
    public boolean occursOn(int year, int month, int day) throws ParseException 
    { 
        DateFormat dateFormatter = new SimpleDateFormat(String.format("yyyy-MM-dd")); 
        Date checkedDate = dateFormatter.parse(String.format("%d-%d-%d", year, month, day)); 
        return checkedDate.equals(this.date); 
    } 
    
	
	// Allow printing of an appointment
    public String toString() 
    { 
    	return String.format("Appointment: %s, Type: One Time, Start Date: %s, End Date: %s", this.description, this.date.toString(), this.date.toString());
    } 
}
